#pip install deep-translator openai streamlit python-dotenv

import streamlit as st
from deep_translator import GoogleTranslator
import openai
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#번역함수
def google_trans(messages):
    return GoogleTranslator(source="auto",target="ko").translate(messages)


def gpt_trans(messages):
    client = openai.OpenAI(api_key = OPENAI_API_KEY)

    messages_prompt = [
        {"role":"system","content":"Translate the following English text into Korean"},
        {"role":"user","content":messages}
    ]

    res = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages_prompt
    )

    return res.choices[0].message.content

def main():
    st.set_page_config(
        page_title="번역을 합니다."
    )

    st.title("번역 비교")

    st.markdown("---")

    st.header("번역을 하고자 하는 텍스트를 입력하세요")
    text = st.text_area(label="",placeholder="input english",height=200)
    st.markdown("---")

    if st.button("번역하기"):
        
        st.text("gpt 번역")
        result = gpt_trans(text)
        st.info(result)

        st.markdown("---")

        st.text("구글번역")
        result1= google_trans(text)
        st.info(result1)



if __name__ == "__main__":
    main()