import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="세균 성장 곡선 시뮬레이터 🧫", page_icon="🦠")

st.title("🦠 세균 성장 곡선 시뮬레이터 (Death phase 포함)")
st.write("조건을 바꿔가며 **세균 성장 곡선**과 **항생제 효과**, 각 성장 단계를 확인해보세요!")

# ---- 조건 선택 ----
N0_option = st.radio("초기 세균 수 (N0)", ["작음", "보통", "많음"])
N0 = {"작음":100, "보통":1000, "많음":5000}[N0_option]

r = st.slider("세균 성장 속도 (r)", 0.1, 1.0, 0.5, 0.1)
d = st.slider("세포 사멸률 (Death rate)", 0.0, 0.05, 0.01, 0.001)

t_option = st.radio("배양 시간", ["짧음", "보통", "김"])
t_max = {"짧음":30, "보통":60, "김":100}[t_option]

K = 100000  # 최대 수용능 고정

# ---- 항생제 투여 여부 및 투여 시점 선택 ----
antibiotic = st.checkbox("항생제 투여")
if antibiotic:
    t_antibiotic = st.slider("항생제 투여 시점 (시간)", 0, t_max, int(t_max*0.1), 1)

# ---- 시뮬레이션 ----
t = np.linspace(0, t_max, 500)
dt = t[1] - t[0]

# 초기값 설정
N_growth = np.zeros_like(t)
N_growth[0] = N0

# 항생제 적용 변수
r_eff = r
K_eff = K

# 시뮬레이션 반복 계산
for i in range(1, len(t)):
    time = t[i]
    # 항생제 투여 시점 이후 성장 억제
    if antibiotic and time >= t_antibiotic:
        r_eff = r * 0.5
        K_eff = K * 0.5
    # 로지스틱 성장 + 사멸률
    N_growth[i] = N_growth[i-1] + (r_eff * N_growth[i-1] * (1 - N_growth[i-1]/K_eff) - d * N_growth[i-1]) * dt
    # 음수 방지
    if N_growth[i] < 0:
        N_growth[i] = 0

# ---- 그래프 출력 ----
fig, ax = plt.subplots(figsize=(8,5))
ax.plot(t, N_growth, label="Bacterial Count", color="blue" if not antibiotic else "red")

# ---- 성장 단계 시각화 ----
lag_end = t_max * 0.1
log_end = t_max * 0.5
stationary_end = t_max * 0.8

ax.axvspan(0, lag_end, color='gray', alpha=0.2, label='Lag phase')
ax.axvspan(lag_end, log_end, color='green', alpha=0.2, label='Log phase')
ax.axvspan(log_end, stationary_end, color='yellow', alpha=0.2, label='Stationary phase')
ax.axvspan(stationary_end, t_max, color='orange', alpha=0.2, label='Death phase')

# 항생제 투여 시점 표시
if antibiotic:
    ax.axvline(x=t_antibiotic, color='purple', linestyle='--', label='Antibiotic Applied')

ax.set_xlabel("Time (hours)")
ax.set_ylabel("Bacterial Count (N)")
ax.set_title("Bacterial Growth Curve with Death Phase and Antibiotic")
ax.legend(loc='upper left', bbox_to_anchor=(1,1))

st.pyplot(fig)

# ---- 단계별 설명 ----
st.subheader("📖 성장 단계 설명")
st.markdown("""
- **유도기 (Lag phase)**: 환경에 적응하는 단계, 성장은 미미함  
- **대수기 (Log phase)**: 세포 분열 활발 → 세균 수 급증  
- **정지기 (Stationary phase)**: 영양분 부족 → 세균 수 일정  
- **사멸기 (Death phase)**: 세포 사멸률 > 증식률 → 세균 수 감소  
""")

# ---- 해석 안내 ----
st.subheader("📊 해석 포인트")
st.markdown("""
- Death rate(d)를 조절하면 사멸기에서 세균 수가 실제로 감소하는 모습을 관찰 가능  
- 항생제 투여 시점과 조건을 바꿔, 성장 억제 효과와 사멸기 변화를 탐구해보세요!
""")
