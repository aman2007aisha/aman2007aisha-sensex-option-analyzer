import streamlit as st
from data_fetcher import get_option_data
from utils import analyze_options

st.set_page_config(page_title="Sensex Option Chain Analyzer", layout="wide")
st.title("📊 Sensex Option Chain Analyzer")

refresh_rate = st.slider("Auto-refresh interval (seconds)", 10, 300, 60)
st.markdown("---")

# Fetching option chain data (mock or live)
data = get_option_data()

# Analyze undervalued options
undervalued_calls, undervalued_puts = analyze_options(data)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔻 Undervalued PUT Options")
    st.dataframe(undervalued_puts)

with col2:
    st.subheader("🔺 Undervalued CALL Options")
    st.dataframe(undervalued_calls)

st.markdown("---")
st.caption("Auto-refresh every {} seconds. Built by ChatGPT 🤖".format(refresh_rate))