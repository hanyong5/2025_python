import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 데이터 (간단한 선형 데이터)
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])  # 정답은 y = 2x

# 초기값
w = 0
b = 0
alpha = 0.01  # 학습률

# 예측 함수
def predict(X):
    return w * X + b

# 손실 함수 (MSE)
def compute_loss(w, b):
    y_pred = w * X + b
    return np.mean((y - y_pred) ** 2)

# 미분(기울기)
def gradients(w, b):
    y_pred = w * X + b
    dw = -2 * np.mean(X * (y - y_pred))
    db = -2 * np.mean(y - y_pred)
    return dw, db

# 그래프 설정
fig, ax = plt.subplots()
line, = ax.plot(X, predict(X), 'r-', label='예측선')
scatter = ax.scatter(X, y, color='blue', label='실제 데이터')
ax.set_ylim(0, 12)
ax.set_title("경사하강법으로 선형회귀 예측선 갱신")
ax.legend()

# 애니메이션 업데이트 함수
def update(frame):
    global w, b
    dw, db = gradients(w, b)
    w -= alpha * dw
    b -= alpha * db
    y_pred = predict(X)
    line.set_ydata(y_pred)
    ax.set_xlabel(f"epoch: {frame}, w: {w:.2f}, b: {b:.2f}")
    return line,

# 애니메이션 실행
ani = FuncAnimation(fig, update, frames=100, interval=200)
plt.show()
