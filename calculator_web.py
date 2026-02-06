import streamlit as st
import pandas as pd

st.set_page_config(page_title="스마트 계산기", page_icon="🧮", layout="centered")

# --- 커스텀 스타일 ---
st.markdown("""
<style>
    .block-container { max-width: 700px; padding-top: 2rem; }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 12px 24px;
        border-radius: 12px 12px 0 0;
        font-size: 1.1rem;
        font-weight: 600;
    }
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 16px;
        color: white;
    }
    div[data-testid="stMetric"] label { color: rgba(255,255,255,0.85) !important; }
    div[data-testid="stMetric"] [data-testid="stMetricValue"] { color: white !important; }
    div[data-testid="stMetric"] [data-testid="stMetricDelta"] { color: #90ee90 !important; }
    .result-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 24px;
        border-radius: 16px;
        text-align: center;
        margin-top: 12px;
    }
    .result-box .expression { font-size: 1.2rem; color: #555; margin-bottom: 8px; }
    .result-box .value { font-size: 2.5rem; font-weight: 700; color: #1a1a2e; }
    .header-container {
        text-align: center;
        padding: 20px 0 10px 0;
    }
    .header-container h1 { font-size: 2.5rem; }
    .header-container p { color: #888; font-size: 1.05rem; }
    .year-table {
        border-radius: 12px;
        overflow: hidden;
        margin-top: 12px;
    }
</style>
""", unsafe_allow_html=True)

# --- 헤더 ---
st.markdown("""
<div class="header-container">
    <h1>🧮 스마트 계산기</h1>
    <p>기본 연산부터 복리 계산까지, 간편하게 사용하세요</p>
</div>
""", unsafe_allow_html=True)

st.divider()

tab1, tab2 = st.tabs(["➕ 기본 계산", "💰 복리 계산"])

# --- 기본 계산 ---
with tab1:
    st.markdown("")
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        a = st.number_input("첫 번째 숫자", value=0.0, key="a", format="%g")
    with col2:
        op = st.selectbox("연산", ["+", "-", "×", "÷", "제곱 (^)", "나머지 (%)"])
    with col3:
        b = st.number_input("두 번째 숫자", value=0.0, key="b", format="%g")

    st.markdown("")
    if st.button("🟰  계산하기", type="primary", use_container_width=True):
        result = None
        error = None
        symbol = op.split()[0] if " " in op else op

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
        elif op == "제곱 (^)":
            symbol = "^"
            result = a ** b
        elif op == "나머지 (%)":
            symbol = "%"
            if b == 0:
                error = "0으로 나눌 수 없습니다."
            else:
                result = a % b

        if error:
            st.error(f"⚠️ {error}")
        elif result is not None:
            st.markdown(f"""
            <div class="result-box">
                <div class="expression">{a:,g} {symbol} {b:,g}</div>
                <div class="value">{result:,g}</div>
            </div>
            """, unsafe_allow_html=True)

# --- 복리 계산 ---
with tab2:
    st.markdown("")
    col1, col2, col3 = st.columns(3)
    with col1:
        principal = st.number_input("💵 원금 (원)", value=1000000.0, min_value=0.0, step=100000.0, format="%g")
    with col2:
        rate = st.number_input("📈 연이율 (%)", value=5.0, min_value=0.0, step=0.1, format="%g")
    with col3:
        years = st.number_input("📅 기간 (년)", value=10.0, min_value=0.0, max_value=100.0, step=1.0, format="%g")

    st.markdown("")
    if st.button("💰  복리 계산하기", type="primary", use_container_width=True):
        total = principal * (1 + rate / 100) ** years
        profit = total - principal

        # 결과 카드
        st.markdown("")
        col1, col2, col3 = st.columns(3)
        col1.metric("💵 원금", f"{principal:,.0f}원")
        col2.metric("💰 최종 금액", f"{total:,.0f}원")
        col3.metric("📈 수익", f"{profit:,.0f}원", delta=f"+{profit / principal * 100:.1f}%" if principal > 0 else None)

        # 연도별 성장 차트
        if years >= 1:
            st.markdown("")
            st.subheader("📊 연도별 자산 성장")
            year_list = list(range(int(years) + 1))
            amounts = [principal * (1 + rate / 100) ** y for y in year_list]
            chart_data = pd.DataFrame({"년도": year_list, "금액 (원)": amounts}).set_index("년도")
            st.area_chart(chart_data, color="#667eea")

# --- 푸터 ---
st.markdown("")
st.divider()
st.markdown(
    "<div style='text-align:center; color:#aaa; font-size:0.85rem;'>"
    "Made with ❤️ using Streamlit"
    "</div>",
    unsafe_allow_html=True,
)
