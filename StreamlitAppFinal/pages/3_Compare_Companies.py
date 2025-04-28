import streamlit as st
import yfinance as yf
import pandas as pd

st.title("🆚 Compare Two Companies")

col1, col2 = st.columns(2)
with col1:
    ticker1 = st.text_input("First Company Ticker (e.g., AAPL)")
with col2:
    ticker2 = st.text_input("Second Company Ticker (e.g., MSFT)")

if ticker1 and ticker2:
    stock1 = yf.Ticker(ticker1).info
    stock2 = yf.Ticker(ticker2).info

    data = {
        "Metric": ["Market Cap", "P/E Ratio", "Dividend Yield"],
        ticker1: [
            stock1.get('marketCap', 'N/A'),
            stock1.get('trailingPE', 'N/A'),
            stock1.get('dividendYield', 'N/A')
        ],
        ticker2: [
            stock2.get('marketCap', 'N/A'),
            stock2.get('trailingPE', 'N/A'),
            stock2.get('dividendYield', 'N/A')
        ]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
