import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Simple Stock Prices", layout="wide")

# Page Title
st.title("📈 Simple Historical Stock Prices")

# Input: Stock Ticker
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", value="AAPL")

# Input: Date Range
start_date = st.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("today"))

# Fetch and display data
if ticker:
    try:
        # Download data
        data = yf.download(ticker, start=start_date, end=end_date)

        if data.empty:
            st.error("No data found for the given ticker and date range.")
        else:
            # Simple Matplotlib line chart
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data.index, data['Close'], label='Close Price', color='blue')
            ax.set_xlabel('Date')
            ax.set_ylabel('Close Price (USD)')
            ax.set_title(f'{ticker} Closing Prices')
            ax.legend()
            ax.grid(True)

            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error loading data: {e}")
