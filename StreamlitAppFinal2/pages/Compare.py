# Importing necessary libraries
import streamlit as st
import pandas as pd

# Setting up the layout and title of the Streamlit page
st.set_page_config(page_title="Compare Two Companies", page_icon="🆚", layout="centered")

# Displaying the main title on the page
st.title("🆚 Compare Two Companies")

# Adding a markdown description 
st.markdown("""
Welcome to the **Company Comparison Tool**!  
Here, you can compare **two companies side-by-side** using key financial metrics.

You can choose from the following companies:
- **Apple (AAPL)**
- **Microsoft (MSFT)**
- **NVIDIA (NVDA)**

### 📘 What You'll See:
We compare three major financial metrics from the Excel file:
- **Market Cap**: Total value of a company’s shares.
- **P/E Ratio (trailingPE)**: How much investors are paying for each dollar of earnings.
- **Dividend Yield**: Income returned to shareholders as a percentage.

Let's get started!
""")

# Dropdown selection for tickers
col1, col2 = st.columns(2)
with col1:
    ticker1 = st.selectbox("First Company", ["AAPL", "MSFT", "NVDA"])
with col2:
    ticker2 = st.selectbox("Second Company", ["AAPL", "MSFT", "NVDA"], index=1)

# Check that the companies selected are not the same
if ticker1 == ticker2:
    st.warning("Please select two different companies.")
else:
    try:
        # Load the Excel file
        df = pd.read_excel("databases/Compare.xlsx")

        # Filter the data to get the selected companies
        selected_df = df[df['Company'].isin([ticker1, ticker2])]

        # Check if both companies are present
        if selected_df.shape[0] != 2:
            st.error("One or both companies are missing from the data file.")
        else:
            # Prepare the comparison table
            data = {
                "Metric": ["Market Cap", "P/E Ratio", "Dividend Yield"],
                ticker1: selected_df[selected_df['Company'] == ticker1][["marketCap", "trailingPE", "divYield"]].values.flatten(),
                ticker2: selected_df[selected_df['Company'] == ticker2][["marketCap", "trailingPE", "divYield"]].values.flatten()
            }

            comparison_df = pd.DataFrame(data)
            st.subheader(f"📊 Side-by-Side Comparison: {ticker1} vs {ticker2}")
            st.dataframe(comparison_df)

    except FileNotFoundError:
        st.error("❌ 'Compare.xlsx' file not found. Please make sure it is in the same folder.")
    except Exception as e:
        st.error(f"🚨 Error loading data: {e}")
