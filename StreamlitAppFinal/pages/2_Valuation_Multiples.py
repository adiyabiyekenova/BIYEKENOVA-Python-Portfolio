import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px

# -------------------
# Streamlit App Layout
# -------------------

st.set_page_config(page_title="Stock Financial Ratio Explorer", page_icon="📈", layout="centered")
st.title("📈 Stock Financial Ratio Explorer")

st.write("Enter a stock ticker to explore its key financial ratios.")

# User Inputs
ticker_input = st.text_input("Enter Stock Ticker (e.g., AAPL, MSFT):", value="AAPL").upper()
selected_ratios = st.multiselect(
    "Select Ratios to Display:",
    ["Return on Equity (ROE)", "Net Profit Margin", "Current Ratio", "Debt-to-Equity", "Asset Turnover"],
    default=["Return on Equity (ROE)", "Net Profit Margin"]
)

# -------------------
# Fetch Financial Data
# -------------------

def get_financial_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        financials = stock.financials
        balance_sheet = stock.balance_sheet
        info = stock.info
        
        return financials, balance_sheet, info
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None, None, None

# -------------------
# Calculate Ratios
# -------------------

def safe_get(balance_sheet, alternatives):
    """Try different row names and return the first match."""
    for alt in alternatives:
        if alt in balance_sheet.index:
            return balance_sheet.loc[alt].iloc[0]
    return np.nan

def calculate_ratios(financials, balance_sheet, info):
    try:
        # Use trailing twelve months (TTM) numbers
        net_income = safe_get(financials, ["Net Income", "NetIncome"])
        total_revenue = safe_get(financials, ["Total Revenue", "TotalRevenue"])
        total_assets = safe_get(balance_sheet, ["Total Assets", "TotalAssets"])
        total_liabilities = safe_get(balance_sheet, ["Total Liabilities Net Minority Interest", "Total Liab", "Total Liabilities"])
        shareholder_equity = safe_get(balance_sheet, ["Total Stockholder Equity", "Ordinary Shares Equity", "Stockholders Equity"])
        current_assets = safe_get(balance_sheet, ["Total Current Assets", "Current Assets"])
        current_liabilities = safe_get(balance_sheet, ["Total Current Liabilities", "Current Liabilities"])

        ratios = {
            "Return on Equity (ROE)": (net_income / shareholder_equity) * 100 if shareholder_equity else np.nan,
            "Net Profit Margin": (net_income / total_revenue) * 100 if total_revenue else np.nan,
            "Current Ratio": (current_assets / current_liabilities) if current_liabilities else np.nan,
            "Debt-to-Equity": (total_liabilities / shareholder_equity) if shareholder_equity else np.nan,
            "Asset Turnover": (total_revenue / total_assets) if total_assets else np.nan
        }
        
        return ratios
    except Exception as e:
        st.error(f"Error calculating ratios: {e}")
        return {}

# -------------------
# Main App Logic
# -------------------

if ticker_input:
    financials, balance_sheet, info = get_financial_data(ticker_input)

    if financials is not None and balance_sheet is not None:
        ratios = calculate_ratios(financials, balance_sheet, info)

        if ratios:
            # Prepare data for selected ratios
            filtered_ratios = {key: ratios[key] for key in selected_ratios if key in ratios}

            if filtered_ratios:
                st.subheader(f"Financial Ratios for {ticker_input}")

                # Create a DataFrame for plotting
                ratio_df = pd.DataFrame.from_dict(filtered_ratios, orient='index', columns=["Value"])
                ratio_df.reset_index(inplace=True)
                ratio_df.rename(columns={"index": "Ratio"}, inplace=True)

                # Plot using Plotly
                fig = px.bar(ratio_df, x="Ratio", y="Value", text_auto='.2f', color="Ratio")
                st.plotly_chart(fig, use_container_width=True)

                # Display table
                st.dataframe(ratio_df.style.format({"Value": "{:.2f}"}))
            else:
                st.warning("Please select at least one ratio to display.")
        else:
            st.warning("Could not calculate ratios for this ticker. Try another one.")
    else:
        st.warning("Invalid ticker or no financial data available.")