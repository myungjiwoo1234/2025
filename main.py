import streamlit as st

# MBTI별 추천 직업 데이터 (예시)
job_data = {
    "INTJ": ["데이터 과학자", "전략 컨설턴트", "연구원"],
    "INFP": ["작가", "상담사", "사회복지사"],
    "ENTP": ["창업가", "마케팅 기획자", "혁신 디자이너"],
    "ISTJ": ["회계사", "법률가", "품질관리자"],
    # ... 나머지 MBTI도 추가
}

# 페이지 제목
st.title("MBTI 기반 진로 추천")

# 사용자 입력
mbti = st.selectbox("당신의 MBTI를 선택하세요", list(job_data.keys()))

# 결과 표시
if mbti:
    st.subheader(f"{mbti} 타입 추천 직업")
    for job in job_data[mbti]:
        st.write(f"- {job}")

    # 추가 설명
    st.info(f"{mbti} 성향을 고려했을 때, 위 직업들은 당신의 강점을 잘 살릴 수 있습니다.")

