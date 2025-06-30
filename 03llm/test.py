import os
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


texts = [
    "파이썬은 매우 인기 있는 프로그래밍 언어입니다.",
    "자연어 처리에서 토큰화는 중요한 단계입니다.",
    "LangChain은 LLM 기반 앱을 쉽게 만들도록 도와줍니다.",
    "벡터 DB는 유사한 문장을 빠르게 검색할 수 있게 합니다.",
    "우리는 백화점 화장실을 찾아줘"
]

docs = [Document(page_content=text) for text in texts ]

# print(docs)

embedding = OpenAIEmbeddings()

faiss_index = FAISS.from_documents(docs,embedding)

print(f"\nFAISS 인덱스 상세 정보:")
print(f"총 문서 수: {faiss_index.index.ntotal}")
print(f"벡터 차원: {faiss_index.index.d}")
print(f"인덱스 타입: {type(faiss_index.index).__name__}")


# 각 문서의 벡터 임베딩 출력 (처음 5개 차원만)
print(f"\n각 문서의 벡터 임베딩 (처음 5개 차원):")
for i, doc in enumerate(docs):
    # 문서의 임베딩 벡터 가져오기
    embedding_vector = embedding.embed_query(doc.page_content)
    print(f"문서 {i+1}: {embedding_vector[:5]}...")


# 5. 검색: 사용자 쿼리와 유사한 문장 찾기
query = "화장실"
docs_and_scores = faiss_index.similarity_search_with_score(query, k=1)

# 6. 결과 출력
for doc, score in docs_and_scores:
    print(f"\n유사도 점수: {score:.4f}")
    print(f"내용: {doc.page_content}")
