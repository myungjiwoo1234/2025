import streamlit as st

# MBTI 직업 추천 데이터 🎯
job_data = {
    "ISTJ": "📊 회계사, 🏛️ 행정가, 🛡️ 경찰관",
    "ISFJ": "👩‍🏫 교사, 🏥 간호사, 📚 사서",
    "INFJ": "🧠 심리상담가, ✍️ 작가, 🌱 환경운동가",
    "INTJ": "💻 데이터 과학자, 🧪 연구원, 📈 전략기획자",
    "ISTP": "🔧 기술자, 🚗 자동차 정비사, 🚓 경찰관",
    "ISFP": "🎨 디자이너, 🎶 음악가, 🌿 조경사",
    "INFP": "📖 소설가, 🧑‍⚕️ 상담가, 🎭 배우",
    "INTP": "🔬 과학자, 🖥️ 프로그래머, 📐 발명가",
    "ESTP": "💼 기업가, 🚓 경찰관, 🎥 영화 프로듀서",
    "ESFP": "🎤 가수, 📺 방송인, 💃 무용가",
    "ENFP": "🌏 여행 작가, 🎨 아티스트, 💡 창업가",
    "ENTP": "🗣️ 토론가, 🚀 스타트업 창업자, 📺 방송인",
    "ESTJ": "🏢 경영자, 🛡️ 군인, 🗂️ 프로젝트 매니저",
    "ESFJ": "🤝 사회복지사, 🏫 교사, 🏥 간호사",
    "ENFJ": "🎓 교육자, 🎤 연설가, 🌍 인권운동가",
    "ENTJ": "📈 CEO, 📊 경영 컨설턴트, 🏛️ 정치가"
}

# 앱 제목 🎉
st.title("🌟 MBTI 기반 직업 추천 사이트 🌟")
st.markdown("### 당신의 MBTI에 맞는 완벽한 직업을 찾아드립니다 💼✨")

# MBTI 선택 💡
mbti_list = list(job_data.keys())
selected_mbti = st.selectbox("🔍 MBTI를 선택하세요:", mbti_list)

# 결과 표시 🎯
if selected_mbti:
    st.markdown(f"## ✨ {selected_mbti} 에 어울리는 직업 추천 ✨")
    st.markdown(f"### {job_data[selected_mbti]}")
    st.markdown("---")
    st.success("💡 MBTI에 맞는 진로를 선택하면 더 행복하고 성공적인 미래를 만들 수 있어요!")

# 푸터 🎨
st.markdown("<p style='text-align:center; font-size:14px;'>💖 Made with Streamlit | MBTI Career Recommender 💖</p>", unsafe_allow_html=True)
