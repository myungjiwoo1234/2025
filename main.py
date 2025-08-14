import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌟", layout="centered")

# MBTI별 직업 데이터
descriptions = {
    "ISTJ": "📊 ISTJ — 꼼꼼하고 책임감 있는 당신! 추천 직업: 회계사, 행정직, 데이터 분석가",
    "ISFJ": "🤝 ISFJ — 헌신과 배려의 아이콘! 추천 직업: 간호사, 상담사, 사회복지사",
    "INFJ": "🔮 INFJ — 통찰력과 이상주의자! 추천 직업: 심리학자, 작가, 인권 변호사",
    "INTJ": "🧠 INTJ — 전략의 설계자! 추천 직업: 연구원, 경영 컨설턴트, 프로그래머",
    "ISTP": "🛠 ISTP — 손재주와 문제 해결력! 추천 직업: 엔지니어, 정비사, 파일럿",
    "ISFP": "🎨 ISFP — 감각과 미의 탐험가! 추천 직업: 디자이너, 사진작가, 음악가",
    "INFP": "🌱 INFP — 이상과 가치의 수호자! 추천 직업: 작가, 예술가, 상담가",
    "INTP": "🔍 INTP — 호기심 많은 사색가! 추천 직업: 과학자, 철학자, 개발자",
    "ESTP": "⚡ ESTP — 모험과 행동파! 추천 직업: 세일즈, 기업가, 스포츠 코치",
    "ESFP": "🎉 ESFP — 분위기 메이커! 추천 직업: 배우, 이벤트 기획자, 방송인",
    "ENFP": "🌈 ENFP — 자유로운 영혼! 추천 직업: 크리에이터, 마케터, 여행 가이드",
    "ENTP": "💡 ENTP — 아이디어 폭발! 추천 직업: 창업가, 광고 기획자, 발명가",
    "ESTJ": "📋 ESTJ — 체계와 조직의 리더! 추천 직업: 관리자, 군 장교, 프로젝트 매니저",
    "ESFJ": "💞 ESFJ — 따뜻한 공동체 지향! 추천 직업: 교사, 간호사, 인사담당자",
    "ENFJ": "🌟 ENFJ — 영감을 주는 리더! 추천 직업: 코치, 강사, 정치인",
    "ENTJ": "🚀 ENTJ — 목표 지향적 지휘관! 추천 직업: CEO, 변호사, 경영 전략가"
}

st.title("🌟 MBTI 진로 추천 사이트 🌟")
st.markdown("""<h4 style='text-align: center;'>MBTI를 선택하면 당신에게 어울리는 직업을 추천해드립니다 ✨</h4>""", unsafe_allow_html=True)

mbti_type = st.selectbox("당신의 MBTI를 선택하세요", list(descriptions.keys()))

if mbti_type:
    st.markdown(f"<div style='font-size: 1.5em; padding: 20px; border-radius: 10px; background-color: #f0f0f5;'>{descriptions[mbti_type]}</div>", unsafe_allow_html=True)
