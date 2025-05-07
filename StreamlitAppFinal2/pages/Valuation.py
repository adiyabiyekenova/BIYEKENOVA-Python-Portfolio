import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Stock Financial Ratio Explorer", page_icon="📈", layout="centered")
st.title("📈 Stock Financial Ratio Explorer")

st.markdown("""
Welcome to the **Stock Financial Ratio Explorer**!  
This app shows you **key financial ratios** for 20 major companies based on pre-loaded data from an Excel file.
""")

# Load Excel data
@st.cache_data
def load_data():
    df = pd.read_excel("Valuation.xlsx")  
    df.set_index("Company", inplace=True)
    return df

# Load the Excel data
data = load_data()

# Company dropdown (from Excel data)
company_list = list(data.index)
selected_company = st.selectbox("🏢 Select a Company:", company_list)

# Ratio selector
selected_ratios = st.multiselect(
    "📌 Select Ratios to Display:",
    ["Return on Equity (ROE)", "Net Profit Margin", "Current Ratio", "Debt-to-Equity", "Asset Turnover"],
    default=["Return on Equity (ROE)", "Net Profit Margin"]
)

# Mapping ratio names to Excel column names
ratio_column_map = {
    "Return on Equity (ROE)": "ROE",
    "Net Profit Margin": "Net Profit Margin",
    "Current Ratio": "Current Ratio",
    "Debt-to-Equity": "D/E Ratio",
    "Asset Turnover": "Asset Turnover"
}

# Filter the data for the selected company and ratios
if selected_company and selected_ratios:
    filtered_data = {
        ratio: data.loc[selected_company, ratio_column_map[ratio]]
        for ratio in selected_ratios
        if ratio_column_map[ratio] in data.columns
    }

    st.subheader(f"📊 Financial Ratios for {selected_company}")

    # Convert to DataFrame for display
    ratio_df = pd.DataFrame.from_dict(filtered_data, orient='index', columns=["Value"])
    ratio_df.reset_index(inplace=True)
    ratio_df.rename(columns={"index": "Ratio"}, inplace=True)

    # Bar chart
    fig = px.bar(ratio_df, x="Ratio", y="Value", text_auto='.2f', color="Ratio")
    st.plotly_chart(fig, use_container_width=True)

    # Table
    st.dataframe(ratio_df.style.format({"Value": "{:.2f}"}))
else:
    st.warning("Please select at least one ratio to display.")

# Explanation of ratios
st.markdown("---")
st.subheader("📚 What Do These Ratios Mean?")
st.markdown("""
**🔹 Return on Equity (ROE):**  
How much profit the company makes from each dollar of shareholder investment. Higher is better.

**🔹 Net Profit Margin:**  
How much of each dollar earned becomes profit.

**🔹 Current Ratio:**  
Compares short-term assets and liabilities. >1 is usually good.

**🔹 Debt-to-Equity:**  
How much a company relies on debt vs. shareholder equity.

**🔹 Asset Turnover:**  
How efficiently the company uses its assets to generate sales.
""")