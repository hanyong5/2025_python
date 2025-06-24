import streamlit as st
from openai import OpenAI

def askGpt(prompt,apiKey):
    client = OpenAI(api_key = apiKey)
    response =  client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"user","content":prompt}
        ]
    )
    summary = response.choices[0].message.content
    return summary


def main():
    st.title("기사 요약 프로그램")
    if 'OPENAI_API' not in st.session_state:
        st.session_state["OPENAI_API"]=''

    with st.sidebar:
        open_apikey = st.text_input(
            label = 'openai api 키',
            placeholder = 'enter your api key',
            value='',
            type='password'
        )

        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
    
    st.markdown("---")
    text = st.text_area('요약 할 글을 입력하세요')

    if st.button("요약"):
        prompt = f'''
            You are an AI specialized in summarizing news articles.  
            Please summarize the following article in **3 concise sentences**, focusing only on the key points.
            Summary Guidelines:  
            - Include key information such as main figures, events, time, location, cause, and outcome  
            - Avoid repetition; keep it concise  
            - Use an objective and neutral tone
            ** text : {text} **
            3-Sentence Summary:
            1.  
            2.  
            3.
            **finally, provide your full answer in korean**
        '''
        st.info(askGpt(prompt,st.session_state['OPENAI_API']))


if __name__ == "__main__":
    main()