# Importing necessary libraries
import streamlit as st
import yfinance as yf # yfinance is used to fetch financial data from Yahoo Finance
import pandas as pd

# Setting up the layout and title of the Streamlit page
st.set_page_config(page_title="Compare Two Companies", page_icon="🆚", layout="centered")

# Displaying the main title on the page using title method
st.title("🆚 Compare Two Companies")

# Adding a markdown description 
st.markdown("""
Welcome to the **Company Comparison Tool**!  
Here, you can compare **two companies side-by-side** using key financial metrics.

This tool is perfect for:
- 📊 Investors deciding between two stocks  
- 📚 Students learning how to evaluate businesses  
- 🤔 Anyone curious about how companies stack up financially

### 📘 What You'll See:
We compare three major financial metrics:
- **Market Cap**: Total value of a company’s shares. A quick snapshot of company size.
- **P/E Ratio (Price-to-Earnings)**: Tells you how much investors are paying for $1 of company earnings. A high P/E can mean high growth expectations—or overvaluation.
- **Dividend Yield**: Shows how much a company pays back to shareholders (as a percentage of its stock price). Ideal for income-focused investors.
""")

# Creating two input columns for the user to enter the ticker symbols of the companies 
col1, col2 = st.columns(2)
with col1:
    ticker1 = st.text_input("First Company Ticker (e.g., AAPL)").upper()  # Input for first company's ticker symbol, converting input to uppercase
with col2:
    ticker2 = st.text_input("Second Company Ticker (e.g., MSFT)").upper()  # Input for second company's ticker symbol, converting input to uppercase

# If both ticker symbols are entered 
if ticker1 and ticker2:
    # Try fetching the financial data for both companies using the yfinance library
    # I accessed company data using the Ticker object, which pulls market cap, P/E ratio, and dividend yield
    try:
        stock1 = yf.Ticker(ticker1).info
        stock2 = yf.Ticker(ticker2).info
        # Create a dictionary (clear and organized) to store the metrics and their values for both companies
        # Get the data and use 'N/A' as a default if data is not available
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
        # Convert the dictionary to a pandas DataFrame for easier visualization
        df = pd.DataFrame(data)
        # Displaying a subheader with the comparison results
        st.subheader(f"📊 Side-by-Side Comparison: {ticker1} vs {ticker2}")
        # Display the comparison table
        st.dataframe(df)

# If there's an error fetching data or performing the comparison, show an error message
    except Exception as e:
        st.error(f"Error fetching data: {e}")