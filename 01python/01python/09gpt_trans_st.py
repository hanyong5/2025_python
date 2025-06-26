#pip install deep-translator
#pip install streamlit
import streamlit as st
from deep_translator import GoogleTranslator


#번역함수
def google_trans(messages):
    return GoogleTranslator(source="auto",target='ko').translate(messages)


#streamlit ui
st.title("영어문장번역")

text = st.text_area("번역할 문장을 입력세요",height=200)

if st.button("번역하기"):
    if text.strip() == "":
        st.warning("번역할 문장을 입력하세요")
    else:
        result = google_trans(text)
        st.success("번역완료")
        st.write(result)
