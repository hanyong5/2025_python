# YouTube 동영상 정보 가져오기 (youtube_transcript_api 대신 pytube 사용)
from pytube import YouTube
import requests
from langchain.schema import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_youtube_info(url):
    """YouTube 동영상의 기본 정보를 가져옵니다."""
    try:
        yt = YouTube(url)
        return {
            'title': yt.title,
            'description': yt.description,
            'author': yt.author,
            'length': yt.length,
            'views': yt.views,
            'publish_date': yt.publish_date
        }
    except Exception as e:
        print(f"에러 발생: {e}")
        return None

def create_documents_from_youtube(url):
    """YouTube 동영상 정보로부터 Document 객체를 생성합니다."""
    video_info = get_youtube_info(url)
    
    if not video_info:
        return []
    
    # 동영상 정보 출력
    print("동영상 제목:", video_info['title'])
    print("채널명:", video_info['author'])
    print("길이:", video_info['length'], "초")
    print("조회수:", video_info['views'])
    print("업로드 날짜:", video_info['publish_date'])
    print("\n설명:", video_info['description'][:500] + "..." if len(video_info['description']) > 500 else video_info['description'])
    
    # Document 객체 생성
    content = f"""제목: {video_info['title']}
채널: {video_info['author']}
길이: {video_info['length']}초
조회수: {video_info['views']}
업로드 날짜: {video_info['publish_date']}

설명:
{video_info['description']}"""
    
    docs = [Document(page_content=content, metadata={
        "source": url, 
        "title": video_info['title'],
        "author": video_info['author'],
        "length": video_info['length'],
        "views": video_info['views']
    })]
    
    return docs

def process_youtube_content(url):
    """YouTube 동영상 내용을 처리하고 분할합니다."""
    # Document 생성
    docs = create_documents_from_youtube(url)
    
    if not docs:
        print("문서를 생성할 수 없습니다.")
        return None, None
    
    print(f"\n문서 생성 완료: {len(docs)}개")
    
    # 텍스트 분할
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(docs)
    
    print(f"분할된 문서 수: {len(split_docs)}")
    print(f"첫 번째 청크 미리보기:\n{split_docs[0].page_content[:300]}...")
    
    return docs, split_docs

# 사용 예시
if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=Pn-W41hC764"
    docs, split_docs = process_youtube_content(url) 