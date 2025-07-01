import os
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

from PyPDF2 import PdfReader
import pandas as pd
import openai



load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

pdf_path = 'data/Summary.pdf'
pdf_reader= PdfReader(pdf_path)

total_text = ''

for page in pdf_reader.pages:
    total_text += page.extract_text()
    # text = page.extract_text()
    # if text:
    #     text = text.replace("\n", " ")
    #     text = " ".join(text.split())
    #     total_text += text+" "

# print(total_text)

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = text_splitter.split_text(total_text)
# print("chunk 갯수 : ",len(chunks))
# print(chunks[2])

text_base = FAISS.from_texts(chunks,OpenAIEmbeddings(
    model="text-embedding-ada-002")
    )
docs = text_base.similarity_search("where can i use chatGPT?")

llm = ChatOpenAI(
    model = 'gpt-3.5-turbo',
    temperature = 0,
    max_tokens = 3000,
)

chain = load_qa_chain(llm,chain_type='stuff')
res = chain.run(input_documents = docs,question = "where can i use chatGPT? 답변은 한글로")

print(res)