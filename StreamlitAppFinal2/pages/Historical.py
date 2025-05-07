# Importing necessary libraries
import streamlit as st  
import matplotlib.pyplot as plt  
import pandas as pd  
from datetime import date

# Streamlit page config
st.set_page_config(page_title="Historical Stock Prices", layout="wide")

# Page title
st.title("📈 Historical Stock Prices")

# Description
st.markdown("""
Welcome to the **Historical Stock Prices** page!

You can choose from **Apple (AAPL)**, **Microsoft (MSFT)**, or **NVIDIA (NVDA)**  
and view how their stock prices have changed from **May 15, 2015** to **May 7, 2025** 📊

This tool helps you:
- Visualize long-term stock trends  
- Spot market shifts  
- Understand real-world event impacts  

Just pick a stock and date range below!
""")

# Dropdown to select a stock
ticker = st.selectbox("🔍 Choose a Stock", ["AAPL", "MSFT", "NVDA"])

# Date range inputs (limited between May 15, 2015 and May 7, 2025)
min_date = date(2015, 5, 15)
max_date = date(2025, 5, 7)

start_date = st.date_input("📅 Start Date", value=min_date, min_value=min_date, max_value=max_date)
end_date = st.date_input("📅 End Date", value=max_date, min_value=min_date, max_value=max_date)

# Ensure valid date range
if start_date > end_date:
    st.error("🚨 Start date must be before end date.")
else:
    try:
        # Load data from the corresponding Excel file
        df = pd.read_excel(f"{ticker}_Stock.xls")

        # Ensure the 'Date' column is datetime
        df['Date'] = pd.to_datetime(df['Date'])

        # Filter by selected date range
        filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

        # If no data in range, show error
        if filtered_df.empty:
            st.error("⚠️ No data available in the selected date range.")
        else:
            # Plotting the data
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(filtered_df['Date'], filtered_df['Close Price'], label='Close Price', color='blue')
            ax.set_xlabel('Date')
            ax.set_ylabel('Close Price (USD)')
            ax.set_title(f'{ticker} Closing Prices')
            ax.grid(True)
            st.pyplot(fig)

    except FileNotFoundError:
        st.error(f"🚫 File {ticker}.xls not found. Please make sure it's in the same folder as this script.")
    except Exception as e:
        st.error(f"🚨 Error loading data: {e}")