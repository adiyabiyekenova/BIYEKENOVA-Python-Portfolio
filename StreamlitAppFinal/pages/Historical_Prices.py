# Importing necessary libraries
import streamlit as st  
import yfinance as yf   # yfinance lets us fetch real-time and historical stock market data from Yahoo Finance
import matplotlib.pyplot as plt  
import pandas as pd  

# Setting up the layout and title of the Streamlit page
st.set_page_config(page_title="Historical Stock Prices", layout="wide")

# Displaying the main title on the page using title method
st.title("📈 Historical Stock Prices")

# Adding a markdown description 
st.markdown("""
Welcome to the **Historical Stock Prices** page!

Here, you can track how a company's stock price has changed over time.  
Just enter the stock ticker symbol (like `AAPL` for Apple or `GOOGL` for Google), choose a start and end date, and we’ll show you a line chart of that company’s closing prices.

This tool is perfect for:
- Visualizing long-term trends 📉📈  
- Spotting major market shifts  
- Learning how real-world events affect stock prices  

Let's get started!
""")

# Input field where users can enter the stock ticker symbol 
# The default value is set to "AAPL"
ticker = st.text_input("🔍 Enter Stock Ticker (e.g., AAPL)", value="AAPL")

# Date input widgets to select start and end dates for the data
# The start date defaults to January 1, 2020, and the end date defaults to today
start_date = st.date_input("📅 Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.date_input("📅 End Date", value=pd.to_datetime("today"))

# Checking if the user has entered a ticker (if the field is non-empty)
if ticker:
    try:
        # Try to fetch stock price data for the ticker and date range using yfinance
        data = yf.download(ticker, start=start_date, end=end_date)

        # If the returned data is empty, that likely means the ticker is invalid or the date range has no data, so return a message 
        if data.empty:
            st.error("⚠️ No data found for the given ticker and date range. Please check your inputs.")
        else:
            # If data exists and can be fetched, creating a figure and axis object using matplotlib for the line chart
            fig, ax = plt.subplots(figsize=(10, 5))  

            # Plotting the 'Close' prices over time
            ax.plot(data.index, data['Close'], label='Close Price', color='blue')

            # Adding axis labels and chart title
            ax.set_xlabel('Date')
            ax.set_ylabel('Close Price (USD)')
            ax.set_title(f'{ticker.upper()} Closing Prices')

            # Rendering the matplotlib figure directly in the Streamlit app
            st.pyplot(fig)

    # If something goes wrong while fetching data or plotting, show an error message
    except Exception as e:
        st.error(f"🚨 Error loading data: {e}")
