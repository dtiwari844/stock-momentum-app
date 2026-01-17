import streamlit as st
import yfinance as yf
import ta

st.title("📈 Stock Momentum Checker")

# Stock input box
stock = st.text_input("Stock likho (Example: RELIANCE.NS)")

# Check button
if st.button("Check"):
    # Stock data download
    df = yf.download(stock, period="5d", interval="15m")

    # EMA and RSI calculation
    df["EMA20"] = ta.trend.ema_indicator(df["Close"], 20)
    df["EMA50"] = ta.trend.ema_indicator(df["Close"], 50)
    df["RSI"] = ta.momentum.rsi(df["Close"], 14)

    last = df.iloc[-1]
    score = 0

    # Momentum logic
    if last["EMA20"] > last["EMA50"]:
        score += 1
    if last["RSI"] > 60:
        score += 1
    if last["Volume"] > df["Volume"].mean():
        score += 1

    # Signal output
    if score >= 2:
        st.success("🔥 Strong Momentum Possible")
    else:
        st.warning("❌ Abhi strong signal nahi")
