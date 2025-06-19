import streamlit as st
import pandas as pd
import numpy as np

from deep_translator import GoogleTranslator


with st.sidebar:
    open_apikey = st.text_input(
        label='openapikey',
        type='password',
        placeholder='openapikey를 입력하세요',
        help='openapikey를 입력하세요'
    )

    if open_apikey:
        st.write(f'openapikey: {open_apikey}')


st.header("요약프로그램")
st.markdown("---")

def translate_text(message):
    google = GoogleTranslator(source='ko', target='en')
    result = google.translate(message)
    return result



text = st.text_area("요약 할 글을 입력")

if st.button("요약하기"):
    translated_text = translate_text(text)
    st.write(translated_text)
    