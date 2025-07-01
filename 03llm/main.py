from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel

import os
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain


from PyPDF2 import PdfReader
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class QuestionRequest(BaseModel):
    question:str


knowledge_base = None

@app.on_event('startup')
def startup_event():
    global knowledge_base
    pdf_path = "data/Summary.pdf"
    knowledge_base = init_knowledge_base(pdf_path)

def init_knowledge_base(pdf_path:str):
    pdf_reader= PdfReader(pdf_path)
    total_text = ''
    for page in pdf_reader.pages:
        total_text += page.extract_text()
    
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200
    )
    chunks = text_splitter.split_text(total_text)
    print(f'chunks count : {len(chunks)} ' )

    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(chunks,embeddings)

@app.post("/ask")
async def ask_question(request:QuestionRequest):
    global knowledge_base
    docs = knowledge_base.similarity_search(request.question)

    llm = ChatOpenAI(
        model = 'gpt-3.5-turbo',
        temperature = 0,
        max_tokens = 3000,
    )

    chain = load_qa_chain(llm,chain_type='stuff')
    res = await run_in_threadpool(chain.run,input_documents=docs,question=request.question)
    return {"answer":res}

