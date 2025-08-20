import streamlit as st

st.set_page_config(page_title="고양이 집사력 테스트 🐾", page_icon="🐱")

# 화면 입장 효과
st.markdown("🎉😸🐾🐱😺😻🎊" * 5)
st.balloons()

st.title("🐱 고양이 집사력 테스트 🐾")
st.write("12가지 질문으로 당신의 집사 점수를 확인해보세요! 😺")

# 세션 상태 초기화
if "answers" not in st.session_state:
    st.session_state.answers = {}

questions = [
    ("1. 고양이가 새벽 3시에 뛰어다닌다면?", [("같이 놀아준다", 3), ("조용히 관찰한다", 2), ("무시한다", 1), ("간식을 준다", 2)]),
    ("2. 고양이가 식탁 위에 올라왔다!", [("바로 내려준다", 3), ("그냥 둔다", 2), ("사진을 찍는다", 2), ("혼낸다", 1)]),
    ("3. 새로운 캣타워를 사주려 한다", [("바로 설치한다", 3), ("상황 봐서 설치한다", 2), ("안 산다", 1), ("간식으로 유도한다", 2)]),
    ("4. 고양이가 창밖을 뚫어져라 본다", [("같이 본다", 3), ("사진 찍는다", 2), ("그냥 둔다", 2), ("창문 닫는다", 1)]),
    ("5. 고양이가 처음 보는 손님을 경계한다면?", [("같이 놀게 한다", 3), ("그냥 두고본다", 2), ("숨게 둔다", 1), ("간식으로 친해지게 한다", 2)]),
    ("6. 고양이가 장난감을 안 건드린다면?", [("새로운 걸 시도한다", 3), ("그냥 둔다", 2), ("원할 때 준다", 2), ("간식으로 유도한다", 1)]),
    ("7. 캣닢을 발견했다!", [("바로 준다", 3), ("상황 봐서 준다", 2), ("필요 없다고 생각한다", 1), ("간식 먼저 준다", 2)]),
    ("8. 고양이가 창문 틈으로 나가려 한다면?", [("같이 막는다", 3), ("그냥 막고 신경 안 쓴다", 2), ("혼낸다", 1), ("간식으로 안 나오게 한다", 2)]),
    ("9. 고양이가 기분이 별로일 때...", [("고양이랑 더 놀아준다", 3), ("그냥 같이 쉰다", 2), ("모른 척 한다", 1), ("간식 챙겨준다", 2)]),
    ("10. 고양이가 갑자기 뛰어와 안긴다면?", [("같이 뛰논다", 3), ("따뜻하게 안아준다", 2), ("어리둥절해한다", 1), ("간식 하나 준다", 2)]),
    ("11. 고양이가 발톱을 세운다면?", [("스크래처 새로 준다", 3), ("그냥 둔다", 2), ("혼낸다", 1), ("간식으로 시선 돌린다", 2)]),
    ("12. 고양이가 밥을 안 먹는다면?", [("새로운 사료를 준다", 3), ("시간 지나면 먹을 거라 생각한다", 2), ("그냥 둔다", 1), ("간식 먼저 준다", 2)])
]

total_score = 0
max_score = len(questions) * 3  # 각 문항 최대 3점

st.header("🐾 질문 시작!")

for i, (q, opts) in enumerate(questions, 1):
    choices = [opt for opt, _ in opts]
    default = st.session_state.answers.get(f"q{i}", choices[0])
    selection = st.radio(f"{i}. {q}", choices, index=choices.index(default), key=f"q{i}")
    st.session_state.answers[f"q{i}"] = selection
    for opt, score in opts:
        if selection == opt:
            total_score += score

if st.button("결과 보기 🐱"):
    final_score = int(total_score / max_score * 100)

    st.subheader("🐾 당신의 집사 점수는...")
    st.success(f"{final_score}점 / 100점 🐱🐾")
    st.progress(final_score)

    if final_score >= 80:
        st.write("🎉 훌륭한 집사! 고양이가 행복할 거예요 😺")
    elif final_score >= 50:
        st.write("🙂 평균적인 집사. 조금 더 신경 쓰면 좋겠어요 🐾")
    else:
        st.write("😿 노력 필요한 집사. 고양이랑 시간을 더 보내세요!")
