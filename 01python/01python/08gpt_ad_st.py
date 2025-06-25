import streamlit as st
import openai


#기능구현함수
def askGpt(prompt,apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"user","content":prompt}
        ])
    gptRes = response.choices[0].message.content
    return gptRes
        
#메인함수
def main():
    st.set_page_config(page_title="광고 문구 생성 프로그램")

    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""

    #사아드바
    with st.sidebar:
        open_apikey=st.text_input(
            label="open api key",
            placeholder = "키를 넣어주세요",
            value='',
            type='password'
        )
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
        st.markdown("---")
    
    st.header("광고 문구 생성 프로그램")
    st.markdown("---")

    col1,col2 = st.columns(2)

    with col1:
        name = st.text_input("제품명",placeholder="제품명")
        #input type=text name=name
        strenghth= st.text_input("특징",placeholder="특징")
        keyword= st.text_input("필수 키워드",placeholder="필수 키워드")


    with col2:
        # com_name = st.text_input("브랜드명",placeholder="브랜드명")
        com_name = st.selectbox(
            "브랜드명",
            options=["삼성","농심","카카오"],
            index=None,
            placeholder="브랜드명 선택"
        )


        tone_manner= st.text_input("톤엔매너",placeholder="발랄하게, 유머스하게, 감성적...")
        value= st.text_input("브랜드핵심가치",placeholder="브랜드핵심가치")

    if st.button("광고문구생성"):
        prompt = f'''
        아래의 내용을 참고해서 1~2줄짜리 광고문구 5개 작성해줘
        - 제품명:{name}
        - 제품특징:{strenghth}
        - 필수포함키워드:{keyword}
        - 브랜드명:{com_name}
        - 톤엔매너:{tone_manner}
        - 브랜드핵심가치:{value}
        '''

        st.info(askGpt(prompt,st.session_state["OPENAI_API"]))


if __name__ == "__main__":
    main()

