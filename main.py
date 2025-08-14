import streamlit as st

# 페이지 기본 세팅
st.set_page_config(page_title="🌟 MBTI 기반 진로 추천", page_icon="💼", layout="centered")

# CSS로 텍스트 스타일 업그레이드
st.markdown("""
<style>
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    background: linear-gradient(90deg, #ff8c00, #ff0080);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    font-size: 20px;
    text-align: center;
    color: #666;
}
.job-card {
    padding: 15px;
    margin: 10px 0;
    border-radius: 15px;
    background: linear-gradient(135deg, #fff0f5, #e0ffff);
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# MBTI별 추천 직업 데이터
job_data = {
    "ISTJ": [
        ("📊 회계사", "정확성과 규율을 중시하는 ISTJ 성향에 딱 맞아요."),
        ("⚖️ 법률가", "체계적인 사고와 규칙 준수를 바탕으로 활약."),
        ("🔍 품질관리자", "세부 사항까지 완벽하게 관리하는 능력.")
    ],
    "ENFP": [
        ("🎨 광고 기획자", "아이디어 폭발 💥, 창의력을 마음껏 발휘!"),
        ("✍️ 작가", "감정을 표현하고 영감을 주는 스토리텔러."),
        ("🚀 창업가", "새로운 도전을 즐기는 모험가 스타일.")
    ],
    "INTJ": [
        ("📈 데이터 과학자", "분석력과 전략적 사고를 결합한 전문가."),
        ("🧠 전략 컨설턴트", "큰 그림을 그리고 실행하는 마스터 플래너."),
        ("🔬 연구원", "깊이 있는 탐구로 세상을 바꾸는 혁신가.")
    ],
    # ... 나머지 MBTI도 동일하게 넣기
}

# 제목
st.markdown('<p class="title">🌟 MBTI 기반 진로 추천 💼</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">당신의 성향에 딱 맞는 직업을 찾아드려요! 🔍</p>', unsafe_allow_html=True)
st.markdown("---")

# 사용자 입력
mbti = st.selectbox("✨ MBTI를 선택하세요", list(job_data.keys()))

# 결과 출력
if mbti:
    st.markdown(f"## 🧾 {mbti} 타입 추천 직업")
    for job, reason in job_data[mbti]:
        st.markdown(f"""
        <div class="job-card">
            <h4>{job}</h4>
            <p>{reason}</p>
        </div>
        """, unsafe_allow_html=True)

    st.success("🌈 당신의 강점을 살릴 수 있는 직업들이에요! 🚀")

    st.balloons()
