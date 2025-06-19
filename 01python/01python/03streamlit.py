import streamlit as st
import pandas as pd
import numpy as np

# st.text("hello streamlit")

# st.title("나의 첫 streamlit")
# st.write("이것은 dataframe 예제입니다.")


# df = pd.DataFrame(
#     np.random.randn(10,2),
#     columns=['x','y']
# )

# st.dataframe(df)
# st.line_chart(df)


st.title("이것이 타이틀입니다.")
st.header("여기는 header")
st.subheader("여기는 subheader")
st.caption("여기는 caption")

sample_code = '''
def funtion():
    print("test")
'''

st.code(sample_code,language='python')
st.text("안녕하세요. text입니다.")

st.markdown("##### 안녕하세요")

sample_table = '''
##### 회원테이블
링크[네이버](https://www.naver.com)

|이름|나이|직업|
|---|---|---|
|한성용ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ|20|사무|

- 이름
1. 홍길동
1. 이순신
1. 이춘식

'''

st.markdown("---")
st.markdown(sample_table)
st.markdown("---")
st.markdown("안녕하세요. **홍길동** 입니다. :blue[파란색] ")

button = st.button('클릭하세요')
if button:
    st.write("안녕하세요. 만나서 반값습니다.")

title = st.text_input(
    label="여행지를 입력하세요",
    placeholder="여행지"
)
st.write(f'당신이 선택한 여행지 {title}')