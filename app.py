import streamlit as st
import yfinance as yf
import ta

st.title("📈 Stock Momentum Checker")

stock = st.text_input("Stock likho (Example: RELIANCE.NS)")

if st.button("Check"):
    df = yf.download(stock, period="5d", interval="15m")

    df["EMA20"] = ta.trend.ema_indicator(df["Close"], 20)
    df["EMA50"] = ta.trend.ema_indicator(df["Close"], 50)
    df["RSI"] = ta.momentum.rsi(df["Close"], 14)

    last = df.iloc[-1]
    score = 0

    if last["EMA20"] > last["EMA50"]: score += 1
    if last["RSI"] > 60: score += 1
    if last["Volume"] > df["Volume"].mean(): score += 1

    if score >= 2:
        st.success("🔥 Strong Momentum Possible")
    else:
        st.warning("❌ Abhi strong signal nahi")
