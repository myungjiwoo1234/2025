import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"  # 설치된 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="세균 성장 곡선 시뮬레이터 🧫", page_icon="🦠")

st.title("🦠 세균 성장 곡선 시뮬레이터")
st.write("조건을 바꿔가며 **세균 성장 곡선**과 **항생제 효과**를 직접 확인해보세요!")

# ---- 조건 선택 ----
N0_option = st.radio("초기 세균 수 (N0)", ["작음", "보통", "많음"])
if N0_option == "작음":
    N0 = 100
elif N0_option == "보통":
    N0 = 1000
else:
    N0 = 5000

r = st.slider("세균 성장 속도 (r)", 0.1, 1.0, 0.5, 0.1)

t_option = st.radio("배양 시간", ["짧음", "보통", "김"])
if t_option == "짧음":
    t_max = 30
elif t_option == "보통":
    t_max = 60
else:
    t_max = 100

K = 100000  # 최대 수용능 고정

# ---- 항생제 투여 여부 선택 ----
antibiotic = st.checkbox("항생제 투여")

# ---- 시뮬레이션 ----
t = np.linspace(0, t_max, 500)

# 정상 성장
N_normal = (K * N0 * np.exp(r*t)) / (K + N0 * (np.exp(r*t) - 1))

# 항생제 투여 (성장 속도 절반, 최대 수용능 절반)
r_antibiotic = r * 0.5
K_antibiotic = K * 0.5
N_antibiotic = (K_antibiotic * N0 * np.exp(r_antibiotic*t)) / (K_antibiotic + N0 * (np.exp(r_antibiotic*t) - 1))

# ---- 선택에 따른 출력 ----
if antibiotic:
    N_growth = N_antibiotic
    label = "항생제 O (성장 억제)"
    color = "red"
else:
    N_growth = N_normal
    label = "항생제 X (정상 성장)"
    color = "blue"

# ---- 그래프 출력 ----
fig, ax = plt.subplots()
ax.plot(t, N_growth, label=label, color=color)
ax.set_xlabel("시간")
ax.set_ylabel("세균 수 (N)")
ax.set_title("세균 성장 곡선")
ax.legend()

st.pyplot(fig)

# ---- 단계별 설명 ----
st.subheader("📖 성장 단계 설명")
st.markdown("""
- **유도기 (Lag phase)**: 환경에 적응하는 단계, 성장은 미미함  
- **대수기 (Log phase)**: 세포 분열 활발 → 세균 수 급증  
- **정지기 (Stationary phase)**: 영양분 부족 → 세균 수 일정  
- **사멸기 (Death phase)**: 세균 사멸률 > 증식률 → 개체 수 감소  
""")

# ---- 해석 안내 ----
st.subheader("📊 해석 포인트")
st.markdown("""
- 항생제를 투여하면 성장 속도와 최대 세균 수가 줄어 세균 증식이 억제됨  
- 라디오 버튼과 슬라이더로 초기 조건을 바꿔보면서, 항생제 효과와 세균 성장 관계를 탐구해보세요!  
- 이를 통해 교과서적 성장 곡선과 실제 조건 변화의 차이를 직관적으로 이해할 수 있습니다.
""")
