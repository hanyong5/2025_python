from fastapi import FastAPI
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