import pandas as pd
from ast import literal_eval
import seaborn as sns
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances


movies_metadata = pd.read_csv("data/movies_metadata.csv")
links_small  = pd.read_csv("data/links_small.csv")
movies_keywords  = pd.read_csv("data/keywords.csv")

links_small = links_small[links_small['tmdbId'].notnull()]["tmdbId"].astype('int')
movies_metadata_small = movies_metadata[movies_metadata['id'].isin(links_small.astype('str'))]

# print(movies_metadata_small.shape)


movies= movies_metadata_small[['id', 'title', 'genres', 'popularity', 'release_date']]

movies['id'] = movies['id'].astype('str')
movies_keywords['id'] = movies_keywords['id'].astype('str')

movies = movies.merge(movies_keywords,on='id')

# print(movies['genres'].loc[0])

movies['genres'] = movies['genres'].fillna('[]').apply(literal_eval) \
                .apply(lambda x: sorted([i['name'] for i in x]) if isinstance(x,list) else [])

movies['keywords'] = movies['keywords'].fillna('[]').apply(literal_eval) \
                .apply(lambda x: sorted([i['name'] for i in x]) if isinstance(x,list) else [])


movies['str_genres_keywords'] = movies['genres'] + movies['keywords']

movies['str_genres_keywords'] = movies['str_genres_keywords'].apply(lambda x: sorted(list(x))) \
                              .apply(lambda x:" ".join(x) if len(x) > 0 else None)


# print(movies['str_genres_keywords'].head())

movies['release_date'] = pd.to_datetime(movies['release_date'], errors='coerce')
movies['year'] = movies['release_date'].dt.year

movies['popularity'] = movies['popularity'].astype(float)
movies['popularity_log'] = np.log(movies['popularity'])

movies = movies.dropna().reset_index(drop=True)

# TF-IDF 메트릭스 생성
tfidf_vectorizer = TfidfVectorizer()
tfidf_mat = tfidf_vectorizer.fit_transform(movies['str_genres_keywords'])
arr_tfidf = tfidf_mat.toarray()
# print(arr_tfidf.shape)

# Euclidean Distances(유클리드 거리)
similarity_of_euclidean = euclidean_distances(arr_tfidf,arr_tfidf)

# print(similarity_of_euclidean.shape)

sorted_similarity_of_euclidean = similarity_of_euclidean.argsort()


def recommendation_of_euclidean(title_name, top_k=5):
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
  return movies.iloc[similar_indexes].sort_values(by=['popularity_log','year'], ascending=False)[:top_k]

recommendation_movies = recommendation_of_euclidean('Robin Hood')

recommendation_movies[['title', 'str_genres_keywords', 'popularity_log', 'year']]
