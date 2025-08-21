import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 기본 설정
st.set_page_config(page_title="세균 성장 실험 🦠💊🐱", page_icon="🐱", layout="centered")

# 타이틀
st.title("🐱🦠 세균 성장 & 항생제 효과 시뮬레이션 💊✨")

# 데이터 생성
time = np.linspace(0, 80, 500)  # 0~80일까지
growth = 1 / (1 + np.exp(-0.2 * (time - 20)))  # 세균 성장
antibiotic_effect = np.where(time > 40, np.exp(-0.1 * (time - 40)), 1)  
population = growth * antibiotic_effect

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor("#FFF5F7")  # 파스텔톤 배경
fig.patch.set_facecolor("#FFF0F5")

ax.plot(time, growth, label="세균 성장 🦠", color="#FF69B4", linewidth=2.5)
ax.plot(time, antibiotic_effect, label="항생제 효과 💊", color="#00CED1", linestyle="--", linewidth=2.5)
ax.plot(time, population, label="실제 개체 수", color="#32CD32", linewidth=3)

# 항생제 투여 시점 표시
ax.axvline(x=40, color="red", linestyle=":", linewidth=2)
ax.text(41, 0.5, "💊 항생제 투여", color="red", fontsize=14)

# 꾸미기
ax.set_xlabel("시간 (일)", fontsize=14, color="#333")
ax.set_ylabel("상대적 세균 수", fontsize=14, color="#333")
ax.set_title("🦠 세균 성장과 항생제 효과 💊", fontsize=18, color="#FF1493", weight="bold")
ax.legend(fontsize=12)

st.pyplot(fig)

# 귀여운 고양이 이모지 눈처럼 떨어지는 효과 (CSS 애니메이션)
st.markdown(
    """
    <style>
    body {
        background-color: #fff0f5;
    }
    .emoji {
        position: fixed;
        top: -50px;
        font-size: 30px;
        animation: fall 8s linear infinite;
    }
    @keyframes fall {
        0% {transform: translateY(-50px);}
        100% {transform: translateY(100vh);}
    }
    </style>
    <div class="emoji" style="left: 10%;">🐱</div>
    <div class="emoji" style="left: 30%;">🐱</div>
    <div class="emoji" style="left: 50%;">🐱</div>
    <div class="emoji" style="left: 70%;">🐱</div>
    <div class="emoji" style="left: 90%;">🐱</div>
    """,
    unsafe_allow_html=True
)
