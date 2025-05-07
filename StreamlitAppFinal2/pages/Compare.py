# Importing necessary libraries
import streamlit as st
import pandas as pd

# Set up the layout and title of the Streamlit page
st.set_page_config(page_title="Compare Two Companies", page_icon="🆚", layout="centered")

# Displaying the main title on the page
st.title("🆚 Compare Two Companies")

# Adding a markdown description 
st.markdown("""
Welcome to the **Company Comparison Tool**!  
You can compare **two major U.S. companies side-by-side** using key financial metrics from our dataset.

### ✅ Available Companies:
- AAPL (Apple)
- MSFT (Microsoft)
- AMZN (Amazon)
- GOOGL (Alphabet)
- META (Meta Platforms)
- TSLA (Tesla)
- BRK.A (Berkshire Hathaway)
- JNJ (Johnson & Johnson)
- JPM (JPMorgan Chase)
- V (Visa)
- PG (Procter & Gamble)
- NVDA (NVIDIA)
- UNH (UnitedHealth Group)
- HD (Home Depot)
- PFE (Pfizer)
- KO (Coca-Cola)
- PEP (PepsiCo)
- INTC (Intel)
- CSCO (Cisco)
- XOM (ExxonMobil)

### 📘 What You'll See:
We compare three key financial metrics:
- **Market Cap**: Total value of all outstanding shares
- **P/E Ratio (Trailing PE)**: Price investors are willing to pay per $1 of earnings
- **Dividend Yield**: Shareholder return as a % of stock price
""")

# List of available tickers
available_tickers = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "META", "TSLA", "BRK.A", "JNJ", "JPM", "V",
    "PG", "NVDA", "UNH", "HD", "PFE", "KO", "PEP", "INTC", "CSCO", "XOM"
]

# User selections
col1, col2 = st.columns(2)
with col1:
    ticker1 = st.selectbox("Select First Company", available_tickers)
with col2:
    ticker2 = st.selectbox("Select Second Company", available_tickers, index=1)

# Check that the companies are not the same
if ticker1 == ticker2:
    st.warning("⚠️ Please select two different companies.")
else:
    try:
        # Load the Excel file
        df = pd.read_excel("Compare.xlsx")

        # Filter to the selected companies
        selected_df = df[df["Company"].isin([ticker1, ticker2])]

        # Ensure both companies exist in the dataset
        if selected_df.shape[0] != 2:
            st.error("❌ One or both companies are missing in the Excel file.")
        else:
            # Prepare comparison data
            data = {
                "Metric": ["Market Cap", "P/E Ratio", "Dividend Yield"],
                ticker1: selected_df[selected_df["Company"] == ticker1][["marketCap", "trailingPE", "divYield"]].values.flatten(),
                ticker2: selected_df[selected_df["Company"] == ticker2][["marketCap", "trailingPE", "divYield"]].values.flatten()
            }

            # Convert to DataFrame for display
            comparison_df = pd.DataFrame(data)
            st.subheader(f"📊 Side-by-Side Comparison: {ticker1} vs {ticker2}")
            st.dataframe(comparison_df)

    except FileNotFoundError:
        st.error("❌ 'Compare.xlsx' not found. Please ensure it is in the same directory as this app.")
    except Exception as e:
        st.error(f"🚨 Error reading data: {e}")
