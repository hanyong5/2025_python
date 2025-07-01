#pip install fastapi
#pip install uvicorn


from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader

from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

# 환경변수 로드
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# FastAPI 앱 초기화
app = FastAPI()

# 전역 변수 초기화
knowledge_base = None

# PDF 읽고 임베딩 생성 (서버 시작 시 1회)
def init_knowledge_base(pdf_path: str):
    pdf_reader = PdfReader(pdf_path)
    total_text = ""
    for page in pdf_reader.pages:
        total_text += page.extract_text()

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(total_text)
    print(f"chunks count: {len(chunks)}")

    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(chunks, embeddings)

# 서버 실행 시 초기화
@app.on_event("startup")
def startup_event():
    global knowledge_base
    pdf_path = "data/Summary.pdf"
    knowledge_base = init_knowledge_base(pdf_path)

# 질문 요청 모델
class QuestionRequest(BaseModel):
    question: str

# 질문 API
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    global knowledge_base
    docs = knowledge_base.similarity_search(request.question)

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=3000,
        request_timeout=120
    )

    chain = load_qa_chain(llm, chain_type="stuff")
    response = chain.run(input_documents=docs, question=request.question)
    return {"answer": response}
