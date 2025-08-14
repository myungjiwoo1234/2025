import streamlit as st
from textwrap import dedent
import random
import json

# =====================
# Page Config
# =====================
st.set_page_config(
    page_title="🌟 MBTI 기반 진로 추천 | 16유형 풀버전",
    page_icon="💼",
    layout="wide",
)

# =====================
# Custom CSS (Fancy!)
# =====================
st.markdown(
    dedent(
        """
        <style>
            /* Background gradient */
            .stApp {
                background: radial-gradient(1200px 600px at 10% 10%, rgba(255, 235, 245, .9), transparent),
                            radial-gradient(1000px 500px at 90% 0%, rgba(230, 255, 250, .9), transparent),
                            linear-gradient(135deg, #f7f7ff 0%, #fff 100%);
            }

            /* Gradient Title */
            .app-title {
                font-size: 48px;
                font-weight: 800;
                text-align: center;
                letter-spacing: 0.5px;
                background: linear-gradient(90deg, #ff8c00, #ff0080, #7c3aed);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin: 0.25rem 0 0.5rem 0;
            }
            .app-subtitle {
                text-align: center;
                font-size: 18px;
                color: #555;
                margin-bottom: 1rem;
            }

            /* Card */
            .card {
                background: linear-gradient(135deg, #ffffff, #f5f0ff);
                border-radius: 20px;
                padding: 18px 18px 14px 18px;
                box-shadow: 0 10px 30px rgba(62, 36, 156, 0.08);
                border: 1px solid rgba(124, 58, 237, 0.1);
                margin-bottom: 14px;
            }
            .chip {
                display: inline-block;
                padding: 6px 10px;
                border-radius: 999px;
                background: rgba(124,58,237,.08);
                border: 1px solid rgba(124,58,237,.15);
                margin: 4px 6px 0 0;
                font-size: 12px;
            }
            .glow {
                text-shadow: 0 0 12px rgba(255, 0, 140, 0.35);
            }
            @keyframes floaty {
                0% { transform: translateY(0px) }
                50% { transform: translateY(-3px) }
                100% { transform: translateY(0px) }
            }
            .floaty { animation: floaty 3s ease-in-out infinite; }

            .muted { color:#666; font-size: 13px }
            .tiny { font-size: 12px; color:#777 }
        </style>
        """
    ),
    unsafe_allow_html=True,
)

# =====================
# Data: 16 types, each with rich items
# =====================
# Each job has: title, reason, skills, paths (majors/certs), vibe emoji
job_data = {
    "ISTJ": {
        "tag": "🧭 현실주의 관리자",
        "jobs": [
            {
                "title": "📊 회계사",
                "reason": "정확성·책임감을 살려 재무 신뢰를 구축합니다.",
                "skills": ["엑셀/데이터", "세법 이해", "리스크 관리"],
                "paths": ["경영·회계", "공인회계사(CPA)"]
            },
            {
                "title": "⚖️ 법무전문가",
                "reason": "규정 준수와 체계적 사고에 강점.",
                "skills": ["논리적 글쓰기", "규정 해석", "분석력"],
                "paths": ["법학", "변호사/법무사"]
            },
            {
                "title": "🔍 품질관리(QA) 매니저",
                "reason": "공정·품질 표준화로 제품 신뢰를 끌어올립니다.",
                "skills": ["표준 운영", "문서화", "세부 집착"],
                "paths": ["산업공학", "품질경영기사"]
            }
        ]
    },
    "ISFJ": {
        "tag": "🛡️ 헌신형 수호자",
        "jobs": [
            {"title": "🏥 간호사", "reason": "세심한 돌봄과 책임감으로 환자 곁을 지킵니다.", "skills": ["커뮤니케이션", "기록 관리", "응급 대응"], "paths": ["간호학", "RN"]},
            {"title": "🍎 교사", "reason": "성실함과 배려로 학습 성장을 돕습니다.", "skills": ["수업 설계", "관찰력", "인내"], "paths": ["교육학", "교원 자격"]},
            {"title": "🤝 사회복지사", "reason": "현장 중심의 지원과 연계에 강점.", "skills": ["사례관리", "자원 연계", "공감"], "paths": ["사회복지학", "사회복지사"]}
        ]
    },
    "INFJ": {
        "tag": "🔮 통찰형 옹호자",
        "jobs": [
            {"title": "🧠 심리상담사", "reason": "깊은 공감과 통찰로 변화를 돕습니다.", "skills": ["경청", "치료 모델", "윤리"], "paths": ["심리학", "상담 자격"]},
            {"title": "✍️ 작가/에디터", "reason": "사람과 사회를 잇는 메시지 전달에 강점.", "skills": ["스토리텔링", "자료조사", "기획"], "paths": ["문예창작", "저널리즘"]},
            {"title": "🌱 비영리 전략가", "reason": "가치 중심 프로젝트를 설계·확산.", "skills": ["기획", "파트너십", "지표 설정"], "paths": ["정책·국제개발", "NPO 경영"]}
        ]
    },
    "INTJ": {
        "tag": "♟️ 전략가",
        "jobs": [
            {"title": "📈 데이터 과학자", "reason": "모델링과 통찰로 의사결정을 가속.", "skills": ["파이썬", "통계/ML", "실험 설계"], "paths": ["데이터사이언스", "수학/통계"]},
            {"title": "🧭 전략 컨설턴트", "reason": "큰 그림과 실행 로드맵을 설계.", "skills": ["문제 분해", "가설 기반", "스토리라인"], "paths": ["경영/산공", "컨설팅"]},
            {"title": "🔬 연구원(R&D)", "reason": "깊이 있는 탐구로 기술 경계 확장.", "skills": ["문헌분석", "실험 디자인", "특허 리서치"], "paths": ["공학/자연과학", "석·박사"]}
        ]
    },
    "ISTP": {
        "tag": "🧰 실전형 해결사",
        "jobs": [
            {"title": "🛠️ 기계/전기 엔지니어", "reason": "현장 문제를 손으로 풀어내는 타입.", "skills": ["CAD", "회로/메카", "트러블슈팅"], "paths": ["공학", "기사 자격"]},
            {"title": "✈️ 파일럿/드론 오퍼레이터", "reason": "정확한 판단·침착함이 강점.", "skills": ["계측/내비", "상황판단", "리스크 관리"], "paths": ["항공 관련", "면장"]},
            {"title": "🔧 정비/테크니션", "reason": "정밀한 손기술과 분석력을 결합.", "skills": ["정밀 공구", "매뉴얼 해석", "품질"], "paths": ["폴리텍/공고", "기술 자격"]}
        ]
    },
    "ISFP": {
        "tag": "🎨 감성형 아티스트",
        "jobs": [
            {"title": "🎨 그래픽/UX 디자이너", "reason": "미감과 섬세함으로 사용자 경험을 빚어냅니다.", "skills": ["Figma", "타이포", "리서치"], "paths": ["디자인", "포트폴리오"]},
            {"title": "🎼 작곡·사운드 디자이너", "reason": "감정의 결을 소리로 설계.", "skills": ["DAW", "믹싱", "음향"], "paths": ["실용음악", "작곡"]},
            {"title": "🐾 수의사", "reason": "동물에 대한 애정 + 실무 능력.", "skills": ["진단", "커뮤니케이션", "기록"], "paths": ["수의학", "국가고시"]}
        ]
    },
    "INFP": {
        "tag": "🌈 이상주의 스토리텔러",
        "jobs": [
            {"title": "✍️ 작가/크리에이터", "reason": "가치와 감정을 설득력 있게 서사화.", "skills": ["카피/에세이", "콘텐츠 기획", "브랜딩"], "paths": ["문예창작", "미디어"]},
            {"title": "🫶 상담사", "reason": "공감·수용·자기성찰 역량.", "skills": ["상담기법", "윤리", "기록"], "paths": ["심리/상담", "자격"]},
            {"title": "🤲 사회복지/국제개발", "reason": "가치 실현·임팩트 지향.", "skills": ["프로그램 설계", "평가", "파트너십"], "paths": ["사회복지/국제학", "NGO"]}
        ]
    },
    "INTP": {
        "tag": "🧪 논리형 아이디어 메이커",
        "jobs": [
            {"title": "💻 소프트웨어 엔지니어", "reason": "복잡한 문제를 구조화해 해결.", "skills": ["자료구조", "알고리즘", "시스템 설계"], "paths": ["컴공", "부트캠프"]},
            {"title": "🔭 이론/응용 연구자", "reason": "가설-검증 사이클을 즐김.", "skills": ["수학적 모델", "시뮬레이션", "논문 작성"], "paths": ["자연과학", "석·박사"]},
            {"title": "🧩 프로덕트 아키텍트", "reason": "개념 설계·추상화에 탁월.", "skills": ["시스템 사고", "API/아키", "문서화"], "paths": ["컴공/산공", "PM/아키"]}
        ]
    },
    "ESTP": {
        "tag": "⚡ 액션 드리븐 플레이어",
        "jobs": [
            {"title": "🗣️ 세일즈/BD 매니저", "reason": "현장 감각·설득·스피드가 무기.", "skills": ["협상", "프리젠", "분석"], "paths": ["경영/마케팅", "세일즈"]},
            {"title": "🚀 창업가", "reason": "기회 포착과 실행의 달인.", "skills": ["린실행", "리스크 감수", "리더십"], "paths": ["무관", "액셀러레이팅"]},
            {"title": "🏅 스포츠 코치/디렉터", "reason": "에너지와 실전 전략을 결합.", "skills": ["코칭", "데이터 분석", "멘탈케어"], "paths": ["체육", "자격"]}
        ]
    },
    "ESFP": {
        "tag": "🎉 무드메이커 퍼포머",
        "jobs": [
            {"title": "🎭 배우·퍼포머", "reason": "사람들과 교감하며 즐거움을 선사.", "skills": ["무대", "발성", "표현"], "paths": ["연극영화", "오디션"]},
            {"title": "🎈 이벤트/행사 기획", "reason": "활발·창의·현장 드리븐.", "skills": ["프로덕션", "스폰서십", "운영"], "paths": ["미디어/이벤트", "포트폴리오"]},
            {"title": "🌍 관광/여행 가이드", "reason": "스토리텔링과 서비스 마인드.", "skills": ["여행지 지식", "안전/일정", "언어"], "paths": ["관광/어문", "가이드"]}
        ]
    },
    "ENFP": {
        "tag": "🚀 아이디어 점프업", 
        "jobs": [
            {"title": "🎨 광고/브랜드 기획", "reason": "아이디어 발산과 크리에이티브 리딩.", "skills": ["캠페인", "카피", "인사이트"], "paths": ["광고/미디어", "에이전시"]},
            {"title": "✍️ 콘텐츠 크리에이터", "reason": "영감과 공감을 연결.", "skills": ["영상/글/오디오", "커뮤니티", "데이터"], "paths": ["무관", "포트폴리오"]},
            {"title": "🚀 스타트업 PM", "reason": "문제 정의→솔루션을 드라이브.", "skills": ["리서치", "우선순위", "실행"], "paths": ["무관", "제품경험"]}
        ]
    },
    "ENTP": {
        "tag": "🪄 아이디어 스파크",
        "jobs": [
            {"title": "🧨 스타트업 CEO/창업가", "reason": "변화·혁신을 주도하는 설득왕.", "skills": ["피치", "전략", "네트워킹"], "paths": ["무관", "액셀러레이터"]},
            {"title": "📣 마케팅 디렉터", "reason": "전략과 크리에이티브의 교차점.", "skills": ["브랜드", "퍼포먼스", "리더십"], "paths": ["마케팅", "현장경험"]},
            {"title": "⚖️ 변호사(특허/IT)", "reason": "논쟁·분석·설득의 교과서.", "skills": ["리서치", "논증", "계약"], "paths": ["법학", "변호사"]}
        ]
    },
    "ESTJ": {
        "tag": "🏗️ 조직형 운영 리더",
        "jobs": [
            {"title": "🏢 경영/운영 매니저", "reason": "프로세스·효율·실행의 챔피언.", "skills": ["프로젝트", "지표", "조정"], "paths": ["경영/산공", "PM"]},
            {"title": "🎯 프로젝트 매니저", "reason": "목표 설정→리스크 관리→딜리버리.", "skills": ["스케줄", "이슈관리", "커뮤니케이션"], "paths": ["무관", "PMP"]},
            {"title": "🪖 군 장교/안전관리", "reason": "규율과 리더십 발휘.", "skills": ["규정", "상황판단", "보고"], "paths": ["관련 학군단", "자격"]}
        ]
    },
    "ESFJ": {
        "tag": "🤗 팀케어 촉진자",
        "jobs": [
            {"title": "🍎 교사/교육 코디네이터", "reason": "협력과 돌봄으로 성장 지원.", "skills": ["교육공학", "상호작용", "평가"], "paths": ["교육학", "교원"]},
            {"title": "🏥 간호/보건교육", "reason": "친절함·체계·팀워크.", "skills": ["진료 보조", "기록", "커뮤니케이션"], "paths": ["간호/보건", "자격"]},
            {"title": "🧩 HR/조직문화", "reason": "사람과 프로세스의 접점을 관리.", "skills": ["채용", "온보딩", "러닝"], "paths": ["경영/심리", "HRD"]}
        ]
    },
    "ENFJ": {
        "tag": "🕊️ 멘토링 리더",
        "jobs": [
            {"title": "🎓 교육 컨설턴트", "reason": "사람의 성장을 전략적으로 설계.", "skills": ["커리큘럼", "코칭", "분석"], "paths": ["교육/심리", "코칭"]},
            {"title": "🌐 커뮤니티 매니저", "reason": "영감을 주고 참여를 이끕니다.", "skills": ["이벤트", "콘텐츠", "데이터"], "paths": ["미디어/사회", "플랫폼"]},
            {"title": "📢 PR/커뮤니케이션", "reason": "관계 확장·이슈 관리.", "skills": ["스토리", "미디어", "위기관리"], "paths": ["커뮤니케이션", "PR"]}
        ]
    },
    "ENTJ": {
        "tag": "🦾 지휘관형 이그제큐터",
        "jobs": [
            {"title": "🏢 기업 경영자/BU 리드", "reason": "목표 지향·의사결정·스케일링.", "skills": ["조직/전략", "재무", "리더십"], "paths": ["경영", "현장 리더십"]},
            {"title": "🎯 전략 기획자", "reason": "큰 그림→성과로 연결.", "skills": ["시장분석", "로드맵", "KPI"], "paths": ["경영/경제", "기획"]},
            {"title": "⚖️ 변호사/정책", "reason": "논리·결단·영향력.", "skills": ["정책/법", "협상", "글쓰기"], "paths": ["법/정치", "자격"]}
        ]
    },
    "ISTP": job_data.get("ISTP"),  # placeholder to ensure key order above worked
}

# NOTE: We already defined ISTP above; but Python dict literal can't refer to itself.
# We'll re-construct cleanly to avoid the placeholder hack.

job_data = {
    "ISTJ": job_data["ISTJ"],
    "ISFJ": job_data["ISFJ"],
    "INFJ": job_data["INFJ"],
    "INTJ": job_data["INTJ"],
    "ISTP": job_data["ISTP"],
    "ISFP": job_data["ISFP"],
    "INFP": job_data["INFP"],
    "INTP": job_data["INTP"],
    "ESTP": job_data["ESTP"],
    "ESFP": job_data["ESFP"],
    "ENFP": job_data["ENFP"],
    "ENTP": job_data["ENTP"],
    "ESTJ": job_data["ESTJ"],
    "ESFJ": job_data["ESFJ"],
    "ENFJ": job_data["ENFJ"],
    "ENTJ": job_data["ENTJ"],
}

# Strengths/Development notes per type (short)
mbti_notes = {
    "ISTJ": ("✅ 강점: 신뢰성·정확성·책임감", "🛠️ 보완: 유연성·창의 협업 시도"),
    "ISFJ": ("✅ 강점: 배려·성실·헌신", "🛠️ 보완: 자기 주장·경계 설정"),
    "INFJ": ("✅ 강점: 통찰·공감·가치 중심", "🛠️ 보완: 완벽주의 완화"),
    "INTJ": ("✅ 강점: 전략·분석·독립성", "🛠️ 보완: 소통·피드백 루프"),
    "ISTP": ("✅ 강점: 실전 문제해결·침착", "🛠️ 보완: 장기계획·협업 공유"),
    "ISFP": ("✅ 강점: 미감·섬세함·유연성", "🛠️ 보완: 목표 설정·협상"),
    "INFP": ("✅ 강점: 가치 추구·공감·창의", "🛠️ 보완: 실행력·우선순위"),
    "INTP": ("✅ 강점: 논리·개념화·탐구", "🛠️ 보완: 마감·커뮤니케이션"),
    "ESTP": ("✅ 강점: 실행·대담함·설득", "🛠️ 보완: 장기지속·문서화"),
    "ESFP": ("✅ 강점: 사교성·현장감·활력", "🛠️ 보완: 체계·재무관리"),
    "ENFP": ("✅ 강점: 창의·영감·연결", "🛠️ 보완: 집중·일관성"),
    "ENTP": ("✅ 강점: 아이디어·토론·전략", "🛠️ 보완: 마무리·운영"),
    "ESTJ": ("✅ 강점: 조직화·효율·리더십", "🛠️ 보완: 경청·유연성"),
    "ESFJ": ("✅ 강점: 협력·케어·조정", "🛠️ 보완: 자기관리·데이터 기반"),
    "ENFJ": ("✅ 강점: 영감·코칭·관계", "🛠️ 보완: 데이터·경계"),
    "ENTJ": ("✅ 강점: 결단·스케일링·야망", "🛠️ 보완: 세부·정서적 감수성"),
}

# Career clusters to quickly filter
clusters = {
    "Tech 💻": ["데이터", "소프트웨어", "아키", "엔지니어"],
    "Biz/Management 📊": ["전략", "경영", "프로젝트", "운영", "PM"],
    "Creative 🎨": ["디자이너", "작가", "크리에이터", "브랜드"],
    "Care/Service 🤝": ["간호", "상담", "사회복지", "교육"],
}

# =====================
# Sidebar Controls
# =====================
st.sidebar.markdown("## ⚙️ 설정")
st.sidebar.markdown("작지만 강력한 필터와 옵션을 사용해 보세요 ✨")

all_types = list(job_data.keys())
selected_type = st.sidebar.selectbox("🔤 MBTI 선택", all_types, index=all_types.index("INTJ") if "INTJ" in all_types else 0)

cluster_pick = st.sidebar.multiselect(
    "🎯 관심 클러스터(복수 선택)", list(clusters.keys()), default=[]
)

show_details = st.sidebar.toggle("🔎 직업 상세(스킬/진로경로) 보기", value=True)

st.sidebar.markdown("---")
if st.sidebar.button("🎲 랜덤 추천 받기"):
    selected_type = random.choice(all_types)
    st.sidebar.success(f"오늘의 랜덤 타입: **{selected_type}** ✨")

# =====================
# Header
# =====================
st.markdown('<div class="app-title floaty">🌟 MBTI 기반 진로 추천 💼</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">당신의 성향에 가장 어울리는 커리어를 이모지와 함께 화려하게 추천합니다 ✨🚀</div>', unsafe_allow_html=True)

# Badges / Chips
_tag = job_data[selected_type]["tag"]
st.markdown(
    f"""
    <div style='text-align:center; margin: .5rem 0 1.25rem 0;'>
        <span class='chip'><b>{selected_type}</b> 타입</span>
        <span class='chip'>{_tag}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# =====================
# Filter logic by cluster keywords
# =====================
items = job_data[selected_type]["jobs"]
if cluster_pick:
    keywords = sum([clusters[c] for c in cluster_pick], [])
    def match(item):
        text = item["title"] + " " + item["reason"]
        return any(kw in text for kw in keywords)
    filtered = list(filter(match, items))
    if filtered:
        items = filtered
    else:
        st.info("선택한 클러스터에 맞는 결과가 없어 전체 결과를 보여드려요 💡")

# =====================
# Notes
# =====================
strong, grow = mbti_notes[selected_type]
st.markdown(
    f"<div class='muted' style='text-align:center'>{strong} &nbsp;&nbsp;|&nbsp;&nbsp; {grow}</div>",
    unsafe_allow_html=True,
)

st.markdown(":sparkles:" * 15)

# =====================
# Main Cards
# =====================
col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

export_payload = {"type": selected_type, "tag": _tag, "recommendations": []}

for i, job in enumerate(items):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"### {job['title']}")
            st.markdown(f"<div class='tiny'>{job['reason']}</div>", unsafe_allow_html=True)
            if show_details:
                st.markdown("— **핵심 스킬**")
                st.markdown(" ".join([f"`{s}`" for s in job["skills"]]))
                st.markdown("— **진로 경로**")
                st.markdown(" ".join([f"`{p}`" for p in job["paths"]]))
        export_payload["recommendations"].append({
            "title": job["title"],
            "reason": job["reason"],
            "skills": job["skills"],
            "paths": job["paths"],
        })

st.balloons()

# =====================
# Download Section
# =====================
st.markdown("---")
st.subheader("📥 결과 저장")
md_lines = [
    f"# {selected_type} — {job_data[selected_type]['tag']}",
    "",
    f"{strong}  ",
    f"{grow}",
    "",
]
for idx, rec in enumerate(export_payload["recommendations"], 1):
    md_lines.append(f"## {idx}. {rec['title']}")
    md_lines.append(f"- 이유: {rec['reason']}")
    md_lines.append(f"- 핵심 스킬: {', '.join(rec['skills'])}")
    md_lines.append(f"- 진로 경로: {', '.join(rec['paths'])}")
    md_lines.append("")

md_text = "\n".join(md_lines)

st.download_button(
    label="💾 마크다운으로 저장 (.md)",
    data=md_text.encode("utf-8"),
    file_name=f"mbti_{selected_type}_career.md",
    mime="text/markdown",
)

st.download_button(
    label="🧩 JSON으로 저장 (.json)",
    data=json.dumps(export_payload, ensure_ascii=False, indent=2).encode("utf-8"),
    file_name=f"mbti_{selected_type}_career.json",
    mime="application/json",
)

# Tiny footer
st.markdown("""
<div class='tiny' style='text-align:center; margin-top: 8px;'>
    ✨ 교육용 참고 자료입니다. 개인의 성향·경험·흥미와 함께 종합적으로 고려해 주세요.
</div>
""", unsafe_allow_html=True)
