import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="세균 성장 곡선 시뮬레이터", page_icon="🦠")

st.title("🦠 세균 성장 곡선 시뮬레이터")

# ---- 사용자 입력 ----
t_max = st.slider("시간 (일)", 10, 100, 60)  # 최대 시간
antibiotic = st.checkbox("항생제 적용 여부", value=False)
t_antibiotic = st.slider("항생제 적용 시점 (일)", 0, t_max, 30) if antibiotic else None

# ---- 세균 성장 모델 ----
t = np.linspace(0, t_max, 500)
N0 = 1e3       # 초기 세균 수
K = 1e6        # 수용한계 (carrying capacity)
r = 0.4        # 성장률

# 로지스틱 성장
N = K / (1 + ((K - N0) / N0) * np.exp(-r * t))

# 사멸기 모델 (stationary 이후 감소)
decay_rate = 0.02
N_decay = N * np.exp(-decay_rate * (t - t_max * 0.8))
N_growth = np.where(t < t_max * 0.8, N, N_decay)

# 항생제 적용 시기 이후 세균 감소
if antibiotic:
    kill_rate = 0.1
    N_growth = np.where(t < t_antibiotic, N_growth, N_growth * np.exp(-kill_rate * (t - t_antibiotic)))

# ---- 그래프 출력 ----
fig, ax = plt.subplots(figsize=(14,7))  # 그래프 영역 크게
ax.plot(t, N_growth, label="Bacterial Count", color="blue" if not antibiotic else "red")

# 성장 단계 시각화
lag_end = t_max * 0.1
log_end = t_max * 0.5
stationary_end = t_max * 0.8

ax.axvspan(0, lag_end, color='gray', alpha=0.2, label='Lag phase')
ax.axvspan(lag_end, log_end, color='green', alpha=0.2, label='Log phase')
ax.axvspan(log_end, stationary_end, color='yellow', alpha=0.2, label='Stationary phase')
ax.axvspan(stationary_end, t_max, color='orange', alpha=0.2, label='Death phase')

if antibiotic:
    ax.axvline(
        x=min(t_antibiotic, t_max - 0.01),  # 끝점일 경우 살짝 왼쪽으로
        color='purple', linestyle='--', label='Antibiotic Applied'
    )

ax.set_xlabel("Time (days)")
ax.set_ylabel("Bacterial Count (N)")
ax.set_title("Bacterial Growth Curve with Death Phase and Antibiotic")

# ✅ x축을 살짝 넓혀서 잘림 방지
ax.set_xlim(0, t_max * 1.05)

# x축 눈금은 그대로 유지
ax.set_xticks(np.linspace(0, t_max, 6))
ax.set_ylim(bottom=0)

ax.legend(loc='upper left', bbox_to_anchor=(1,1))
st.pyplot(fig)
