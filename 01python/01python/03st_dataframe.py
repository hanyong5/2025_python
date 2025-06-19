import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("안녕하세요_han")
st.header("여기는 header")
st.text("안녕하세요. 여기는 text")

df = pd.DataFrame({
    "first":[1,2,3,4],
    "second":[10,20,30,40]
})

# st.dataframe(df)
# st.table(df)

# st.metric(label="온도",value="10",delta="1.2")
# st.metric(label="삼성전자",value="60,000",delta="-1.2")


# fig,ax = plt.subplots()
# ax.plot(df)
# st.pyplot(fig)


# st.line_chart(df)
# st.bar_chart(df)

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# st.dataframe(chart_data)

# st.bar_chart(chart_data)


text = ""

name = '홍길동'

button = st.button("버튼")

if button:
    st.write(f'안녕하세요. {name} 님 만나서 반갑습니다.')

title = st.text_input(
    label='여행지입력',
    placeholder='원하는 여행지를 입력하세요'
)
if title:
    st.write(f'{name} 님이 원하시는 여행지는 {title}이 맞나요')

st.download_button(
    label='csv다운',
    data=df.to_csv(),
    file_name='sample.csv',
    mime='text/csv'
)

agree = st.checkbox('동의를 원하나요?')
if agree:
    st.write("동의 감사합니다.")

mbti = st.radio(
    '당신의 mbti는 무엇입니까?',
    ('istj','enfp','no'),
    index=2,
    horizontal=True
)

if mbti == 'istj':
    st.write("당신은 현실주의자이시네요")
elif mbti == 'enfp':
    st.write("당신은 활동가 이시네요")
else:
    st.write("당신의 다시선택하세요")


col1,col2,col3 = st.columns([1,3,1])

with col1:
    st.header("col1")
    st.text("안녕하세요 여기는 col1")
    st.image("https://s.pstatic.net/shopping.phinf/20250520_27/fce73aa7-8602-4ebd-9b3e-74b40758e9b7.jpg?type=f294_378")

with col2:
    st.header("col1")
    st.image('https://s.pstatic.net/dthumb.phinf/?src=%22https%3A%2F%2Fs.pstatic.net%2Fimgnews%2Fimage%2F144%2F2025%2F06%2F18%2F0001047164_001_20250618101415758.png%22&type=nf370_208&service=navermain')

with col3:
    st.header("col1")


tab1,tab2,tab3 = st.tabs(["Cat","Dog","Owl"])

with tab1:
    st.header("cat")
    st.text("jfkdlsa;jkfdlasjfkld;asjl;fddajlsfd")

with tab2:
    st.header("dog")
    st.text("jfkdlsa;jkfdlasjfkld;asjl;fddajlsfd")

with tab3:
    st.header("owl")
    st.text("jfkdlsa;jkfdlasjfkld;asjl;fddajlsfd")




with st.sidebar:
    st.header("여기는 사이드바")