import random
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="오늘의 띠별 운세", page_icon="✨", layout="centered"
)

# 화면 구성
st.title("✨ 오늘의 띠별 운세 ✨")
st.write("자신의 띠를 선택하고 오늘의 운세를 확인해 보세요!")

# 띠 목록 및 데이터
zodiac_signs = [
    "쥐띠",
    "소띠",
    "호랑이띠",
    "토끼띠",
    "용띠",
    "뱀띠",
    "말띠",
    "양띠",
    "원숭이띠",
    "닭띠",
    "개띠",
    "돼지띠",
]

fortunes = [
    "오늘은 뜻밖의 기회가 찾아오는 날입니다. 자신감을 갖고 도전해 보세요!",
    "주변 사람들과의 소통이 중요한 하루입니다. 작은 배려가 큰 행운으로 돌아옵니다.",
    "급할수록 돌아가라는 말이 있듯이, 차분하게 일처리를 하는 것이 유리합니다.",
    "재물운이 상승하는 하루입니다. 다만, 불필요한 지출은 주의하세요.",
    "새로운 인연을 만나거나 반가운 소식을 들을 수 있는 활기찬 하루입니다.",
    "잠시 휴식을 취하며 에너지를 재충전하는 시간을 가져보세요. 건강이 최우선입니다.",
]

colors = ["빨간색", "파란색", "초록색", "노란색", "보라색", "흰색", "검은색"]
numbers = [3, 7, 8, 12, 19, 24, 33]

# 띠 선택 박스
selected_zodiac = st.selectbox("당신의 띠를 선택해주세요:", zodiac_signs)

if st.button("운세 확인하기", type="primary"):
  random.seed(selected_zodiac + "2026")

  fortune = random.choice(fortunes)
  color = random.choice(colors)
  number = random.choice(numbers)
  score = random.randint(75, 98)

  st.divider()

  st.subheader(f"🔮 {selected_zodiac}의 오늘의 운세")
  st.metric(label="오늘의 운세 점수", value=f"{score}점")

  st.info(f"**총운:** {fortune}")

  col1, col2 = st.columns(2)
  with col1:
    st.success(f"🍀 행운의 색상: **{color}**")
  with col2:
    st.warning(f"🔢 행운의 숫자: **{number}**")