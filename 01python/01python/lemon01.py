import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


st.title('레모네이드 판매량 예측기')

lemon = pd.read_csv("data/lemonade01.csv")

#데이터 전처리
X = lemon[['온도']]
y = lemon['판매량']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# 모델 생성
model = LinearRegression()

# 모델 데이터 fit
model.fit(X_train,y_train)


# y_pred = model.predict(X_test)
# st.text(y_pred)


input_temp = st.number_input("예측할 온도 입력",min_value=20,max_value=50,step=1)

if st.button("판매량 예측"):
    pred = model.predict([[input_temp]])
    st.text(pred)
    st.success(f'예상판매량 : {pred[0]} 잔')





# 모델 예측
# y_pred = model.predict(X_test)



