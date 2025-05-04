# Importing necessary libraries
import streamlit as st
import yfinance as yf # yfinance is used to fetch stock data from Yahoo Finance
import pandas as pd
import numpy as np # numpy is used for numerical operations
import plotly.express as px # plotly.express is used for creating interactive charts

# Set up the layout of the Streamlit page
st.set_page_config(page_title="Stock Financial Ratio Explorer", page_icon="📈", layout="centered")
# Display the main title on the page using title method
st.title("📈 Stock Financial Ratio Explorer")

# Use markdown to introduce the page
st.markdown("""
Welcome to the **Stock Financial Ratio Explorer**!  
This page helps you understand how a company is performing by looking at **key financial ratios**.

Just type in a stock ticker (like `AAPL` or `MSFT`), choose which ratios you want to explore, and we'll show you colorful charts and numbers to help you make sense of it all.

This is perfect for:
- 📊 Comparing financial health
- 🧠 Learning how investors judge companies
- 📚 Studying real companies in action
""")

# Create a text input box for the user to enter a stock ticker, default is set to 'AAPL' and converting input to uppercase
ticker_input = st.text_input("🔍 Enter Stock Ticker (e.g., AAPL, MSFT):", value="AAPL").upper()
# Create a multi-select dropdown for the user to choose which financial ratios to display
selected_ratios = st.multiselect(
    "📌 Select Ratios to Display:", # Label
    ["Return on Equity (ROE)", "Net Profit Margin", "Current Ratio", "Debt-to-Equity", "Asset Turnover"], # List of available ratios
    default=["Return on Equity (ROE)", "Net Profit Margin"] # Default selected ratios
)

# Function to fetch the financial data for a given ticker symbol
def get_financial_data(ticker):
    try:
        stock = yf.Ticker(ticker) # Initialize the Ticker object from yfinance
        financials = stock.financials # Fetch the financial data
        balance_sheet = stock.balance_sheet # Fetch the balance sheet data
        info = stock.info # Fetch general information about the company 
        return financials, balance_sheet, info # Return the fetched data
    except Exception as e: # If there's an error fetching data display the error
        st.error(f"Error fetching data: {e}")
        return None, None, None # Return None for all data if an error occurs

# Function to safely extract data from the balance sheet (there may be different column names)
def safe_get(balance_sheet, alternatives):
    for alt in alternatives:
        if alt in balance_sheet.index:  # Check if any alternative column is present
            return balance_sheet.loc[alt].iloc[0] # Return the first value in the column
    return np.nan # If no value is found, return NaN

# Function to calculate the selected financial ratios
def calculate_ratios(financials, balance_sheet, info):
    try:
        # Extracting relevant values from financials and balance sheet using safe_get function
        net_income = safe_get(financials, ["Net Income", "NetIncome"])
        total_revenue = safe_get(financials, ["Total Revenue", "TotalRevenue"])
        total_assets = safe_get(balance_sheet, ["Total Assets", "TotalAssets"])
        total_liabilities = safe_get(balance_sheet, ["Total Liabilities Net Minority Interest", "Total Liab", "Total Liabilities"])
        shareholder_equity = safe_get(balance_sheet, ["Total Stockholder Equity", "Ordinary Shares Equity", "Stockholders Equity"])
        current_assets = safe_get(balance_sheet, ["Total Current Assets", "Current Assets"])
        current_liabilities = safe_get(balance_sheet, ["Total Current Liabilities", "Current Liabilities"])
        
        # Calculating the financial ratios using the extracted data and putting in a dictionary
        ratios = {
            "Return on Equity (ROE)": (net_income / shareholder_equity) * 100 if shareholder_equity else np.nan,
            "Net Profit Margin": (net_income / total_revenue) * 100 if total_revenue else np.nan,
            "Current Ratio": (current_assets / current_liabilities) if current_liabilities else np.nan,
            "Debt-to-Equity": (total_liabilities / shareholder_equity) if shareholder_equity else np.nan,
            "Asset Turnover": (total_revenue / total_assets) if total_assets else np.nan
        }
        return ratios # Return the calculated ratios
    except Exception as e:
        # If there is an error calculating ratios display the error
        st.error(f"Error calculating ratios: {e}")
        return {} # Return an empty dictionary if there was an error

# If the user has entered a ticker symbol, proceed with fetching and calculating the data
if ticker_input:
    financials, balance_sheet, info = get_financial_data(ticker_input)
    
    # If data was successfully fetched
    if financials is not None and balance_sheet is not None:
        ratios = calculate_ratios(financials, balance_sheet, info) # Calculate the ratios
        
        # If there are ratios to display
        if ratios:
            # Filter the ratios based on the user's selection
            filtered_ratios = {key: ratios[key] for key in selected_ratios if key in ratios}
            
            # If there are any filtered ratios to show
            if filtered_ratios:
                st.subheader(f"📊 Financial Ratios for {ticker_input}") # Display a subheader with the ticker name
                # Convert the ratios dictionary into a pandas DataFrame for display
                ratio_df = pd.DataFrame.from_dict(filtered_ratios, orient='index', columns=["Value"])
                ratio_df.reset_index(inplace=True)
                ratio_df.rename(columns={"index": "Ratio"}, inplace=True)
                # Create an interactive bar chart using Plotly to visualize the ratios
                fig = px.bar(ratio_df, x="Ratio", y="Value", text_auto='.2f', color="Ratio")
                st.plotly_chart(fig, use_container_width=True) # Display the bar chart
                # Display the data in a styled table format
                st.dataframe(ratio_df.style.format({"Value": "{:.2f}"}))
            else:
                # If no ratios were selected or no data was found, display a warning
                st.warning("Please select at least one ratio to display.")
        else:
             # If no valid ratios were calculated, display a warning
            st.warning("Could not calculate ratios for this ticker. Try another one.")
    else:
        # If financial data could not be fetched, display a warning
        st.warning("Invalid ticker or no financial data available.")

# Add a markdown section with explanations for each of the financial ratios
st.markdown("---")
st.subheader("📚 What Do These Ratios Mean?")
st.markdown("""
**🔹 Return on Equity (ROE):**  
How much profit the company makes from each dollar of shareholder investment. Higher is better.

**🔹 Net Profit Margin:**  
How much of each dollar earned becomes profit. For example, a 20% margin means the company keeps 0.20 USD for every 1 USD it earns.

**🔹 Current Ratio:**  
Can the company pay its bills? This ratio compares what it owns short-term vs. what it owes short-term. A ratio >1 is good.

**🔹 Debt-to-Equity:**  
How much the company relies on borrowing (debt) vs. owners' money (equity). Lower is often safer.

**🔹 Asset Turnover:**  
How good is the company at using its assets to make sales? Higher values mean it's efficient.
""")