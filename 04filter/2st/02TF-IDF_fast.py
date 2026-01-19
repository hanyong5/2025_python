import pandas as pd
from ast import literal_eval
import seaborn as sns
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI(title="Movie Recommendation API", version="1.0.0")


def load_data():
    """데이터 파일 로드"""
    movies_metadata = pd.read_csv("data/movies_metadata.csv")
    links_small = pd.read_csv("data/links_small.csv")
    movies_keywords = pd.read_csv("data/keywords.csv")

    return movies_metadata, links_small, movies_keywords


def preprocess_data(movies_metadata, links_small, movies_keywords):
    """데이터 전처리 및 특성 엔지니어링"""
    # 유효한 영화 ID 필터링
    links_small = links_small[links_small['tmdbId'].notnull()]["tmdbId"].astype('int')
    movies_metadata_small = movies_metadata[movies_metadata['id'].isin(links_small.astype('str'))]

    # 필요한 컬럼만 선택
    movies = movies_metadata_small[['id', 'title', 'genres', 'popularity', 'release_date']]

    # ID 타입 변환 및 병합
    movies['id'] = movies['id'].astype('str')
    movies_keywords['id'] = movies_keywords['id'].astype('str')
    movies = movies.merge(movies_keywords, on='id')

    # 장르 처리
    movies['genres'] = movies['genres'].fillna('[]').apply(literal_eval) \
                    .apply(lambda x: sorted([i['name'] for i in x]) if isinstance(x, list) else [])

    # 키워드 처리
    movies['keywords'] = movies['keywords'].fillna('[]').apply(literal_eval) \
                    .apply(lambda x: sorted([i['name'] for i in x]) if isinstance(x, list) else [])

    # 장르와 키워드 결합
    movies['str_genres_keywords'] = movies['genres'] + movies['keywords']
    movies['str_genres_keywords'] = movies['str_genres_keywords'].apply(lambda x: sorted(list(x))) \
                                  .apply(lambda x: " ".join(x) if len(x) > 0 else None)

    # 날짜 및 연도 처리
    movies['release_date'] = pd.to_datetime(movies['release_date'], errors='coerce')
    movies['year'] = movies['release_date'].dt.year

    # 인기도 로그 변환
    movies['popularity'] = movies['popularity'].astype(float)
    movies['popularity_log'] = np.log(movies['popularity'])

    # 결측치 제거
    movies = movies.dropna().reset_index(drop=True)

    return movies


def create_tfidf_matrix(movies):
    """TF-IDF 매트릭스 생성"""
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_mat = tfidf_vectorizer.fit_transform(movies['str_genres_keywords'])
    arr_tfidf = tfidf_mat.toarray()

    return arr_tfidf


def calculate_similarity(arr_tfidf):
    """유클리드 거리 기반 유사도 계산"""
    similarity_of_euclidean = euclidean_distances(arr_tfidf, arr_tfidf)
    sorted_similarity_of_euclidean = similarity_of_euclidean.argsort()

    return sorted_similarity_of_euclidean


def recommendation_of_euclidean(movies, sorted_similarity_of_euclidean, title_name, top_k=5):
    """유클리드 거리 기반 영화 추천"""
    # 기준 영화 추출
    movie_of_title = movies[movies['title'] == title_name]
    print(f"{title_name}의 장르: {movie_of_title['str_genres_keywords'].values[0]}")

    # 기준 영화 인덱스
    movie_index_of_title = movie_of_title.index.values[0]

    # 기준 영화를 기준으로 가장 유사도가 높은 영화들의 인덱스 추출
    similar_indexes = sorted_similarity_of_euclidean[movie_index_of_title, :(top_k*2)]
    # 메트릭스(2차원의 데이터)를 벡터(1차원의 데이터)로 변환
    similar_indexes = similar_indexes.reshape(-1)
    # 기준 영화 인덱스는 제외
    similar_indexes = similar_indexes[similar_indexes != movie_index_of_title]

    # 유사도 기반으로 추출된 영화 추천
    return movies.iloc[similar_indexes].sort_values(by=['popularity_log', 'year'], ascending=False)[:top_k]


# FastAPI 앱 초기화
app = FastAPI(title="Movie Recommendation API", version="1.0.0")

# 전역 변수로 데이터 저장
movies_data = None
similarity_matrix = None


# Pydantic 모델 정의
class MovieRecommendationRequest(BaseModel):
    title: str
    top_k: Optional[int] = 5


class MovieInfo(BaseModel):
    title: str
    str_genres_keywords: str
    popularity_log: float
    year: int


class MovieRecommendationResponse(BaseModel):
    query_movie: str
    genres: str
    recommendations: List[MovieInfo]


@app.on_event("startup")
async def startup_event():
    """앱 시작 시 데이터 로드 및 전처리"""
    global movies_data, similarity_matrix

    print("데이터 로딩 중...")
    # 데이터 로드
    movies_metadata, links_small, movies_keywords = load_data()

    print("데이터 전처리 중...")
    # 데이터 전처리
    movies_data = preprocess_data(movies_metadata, links_small, movies_keywords)

    print("TF-IDF 매트릭스 생성 중...")
    # TF-IDF 매트릭스 생성
    arr_tfidf = create_tfidf_matrix(movies_data)

    print("유사도 계산 중...")
    # 유사도 계산
    similarity_matrix = calculate_similarity(arr_tfidf)

    print("서버 준비 완료!")


@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {
        "message": "Movie Recommendation API",
        "endpoints": {
            "/recommend": "POST - 영화 추천",
            "/movies": "GET - 전체 영화 목록",
            "/movies/{title}": "GET - 특정 영화 정보"
        }
    }


@app.post("/recommend", response_model=MovieRecommendationResponse)
async def recommend_movies(request: MovieRecommendationRequest):
    """영화 추천 엔드포인트"""
    global movies_data, similarity_matrix

    if movies_data is None or similarity_matrix is None:
        raise HTTPException(status_code=503, detail="서버가 아직 준비 중입니다.")

    # 영화 존재 여부 확인
    if request.title not in movies_data['title'].values:
        raise HTTPException(status_code=404, detail=f"'{request.title}' 영화를 찾을 수 없습니다.")

    # 영화 추천
    try:
        movie_info = movies_data[movies_data['title'] == request.title].iloc[0]
        recommendation_df = recommendation_of_euclidean(
            movies_data,
            similarity_matrix,
            request.title,
            request.top_k
        )

        # 결과 변환
        recommendations = []
        for _, row in recommendation_df.iterrows():
            recommendations.append(MovieInfo(
                title=row['title'],
                str_genres_keywords=row['str_genres_keywords'],
                popularity_log=float(row['popularity_log']),
                year=int(row['year'])
            ))

        return MovieRecommendationResponse(
            query_movie=request.title,
            genres=movie_info['str_genres_keywords'],
            recommendations=recommendations
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"추천 처리 중 오류 발생: {str(e)}")


@app.get("/movies")
async def get_movies(limit: Optional[int] = 10, offset: Optional[int] = 0):
    """전체 영화 목록 조회"""
    global movies_data

    if movies_data is None:
        raise HTTPException(status_code=503, detail="서버가 아직 준비 중입니다.")

    total = len(movies_data)
    movies_subset = movies_data.iloc[offset:offset+limit]

    movies_list = []
    for _, row in movies_subset.iterrows():
        movies_list.append({
            "title": row['title'],
            "genres": row['str_genres_keywords'],
            "year": int(row['year']),
            "popularity_log": float(row['popularity_log'])
        })

    return {
        "total": total,
        "offset": offset,
        "limit": limit,
        "movies": movies_list
    }


@app.get("/movies/{title}")
async def get_movie_info(title: str):
    """특정 영화 정보 조회"""
    global movies_data

    if movies_data is None:
        raise HTTPException(status_code=503, detail="서버가 아직 준비 중입니다.")

    movie = movies_data[movies_data['title'] == title]

    if len(movie) == 0:
        raise HTTPException(status_code=404, detail=f"'{title}' 영화를 찾을 수 없습니다.")

    movie_row = movie.iloc[0]

    return {
        "title": movie_row['title'],
        "genres": movie_row['str_genres_keywords'],
        "year": int(movie_row['year']),
        "popularity_log": float(movie_row['popularity_log'])
    }


def main():
    """메인 실행 함수 (개발/테스트용)"""
    # 데이터 로드
    movies_metadata, links_small, movies_keywords = load_data()

    # 데이터 전처리
    movies = preprocess_data(movies_metadata, links_small, movies_keywords)

    # TF-IDF 매트릭스 생성
    arr_tfidf = create_tfidf_matrix(movies)

    # 유사도 계산
    sorted_similarity_of_euclidean = calculate_similarity(arr_tfidf)

    # 영화 추천
    recommendation_movies = recommendation_of_euclidean(movies, sorted_similarity_of_euclidean, 'Robin Hood')

    # 결과 출력
    print(recommendation_movies[['title', 'str_genres_keywords', 'popularity_log', 'year']])


if __name__ == '__main__':
    import uvicorn
    # FastAPI 서버 실행
    uvicorn.run(app, host="0.0.0.0", port=8000)
