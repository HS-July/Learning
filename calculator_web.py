import streamlit as st

st.set_page_config(page_title="계산기", page_icon="🧮")
st.title("🧮 계산기")

tab1, tab2 = st.tabs(["기본 계산", "복리 계산"])

with tab1:
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        a = st.number_input("첫 번째 숫자", value=0.0, key="a")
    with col2:
        op = st.selectbox("연산", ["+", "-", "×", "÷", "**", "%"])
    with col3:
        b = st.number_input("두 번째 숫자", value=0.0, key="b")

    if st.button("계산하기", type="primary", use_container_width=True):
        result = None
        error = None
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "×":
            result = a * b
        elif op == "÷":
            if b == 0:
                error = "0으로 나눌 수 없습니다."
            else:
                result = a / b
        elif op == "**":
            result = a ** b
        elif op == "%":
            if b == 0:
                error = "0으로 나눌 수 없습니다."
            else:
                result = a % b

        if error:
            st.error(error)
        elif result is not None:
            st.success(f"결과: {a:,g} {op} {b:,g} = **{result:,g}**")

with tab2:
    principal = st.number_input("원금 (원)", value=1000000.0, min_value=0.0, step=100000.0)
    rate = st.number_input("연이율 (%)", value=5.0, min_value=0.0, step=0.1)
    years = st.number_input("기간 (년)", value=10.0, min_value=0.0, step=1.0)

    if st.button("복리 계산하기", type="primary", use_container_width=True):
        total = principal * (1 + rate / 100) ** years
        profit = total - principal

        col1, col2 = st.columns(2)
        col1.metric("최종 금액", f"{total:,.0f}원")
        col2.metric("수익", f"{profit:,.0f}원", delta=f"{profit/principal*100:.1f}%")
