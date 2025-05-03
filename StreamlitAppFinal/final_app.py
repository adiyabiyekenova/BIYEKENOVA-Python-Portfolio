import streamlit as st

# Set up page configuration
st.set_page_config(page_title="Investment Insights App", layout="wide")

# Title & Subtitle
st.markdown("<h1 style='text-align: center;'>📊 Investment Insights App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: grey;'>Visualize, Compare, and Analyze Financial Data with Ease</h4>", unsafe_allow_html=True)
st.write("---")

# Layout with columns
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2463/2463510.png", width=150)  # Optional decorative icon
    st.markdown(
        """
        Welcome to the **Investment Insights App**!  
        This app is designed for finance professionals and enthusiasts to:
        - 📈 View historical stock prices  
        - 🏢 Compare companies using key financial ratios  
        - 💰 Explore valuation multiples  
        
        Whether you're preparing a pitchbook, conducting valuation, or learning finance — this tool helps you do it faster and smarter.
        """
    )

    # Add 3 buttons for navigation
    st.write("---")  # Divider between sections

    st.markdown("<h4 style='text-align: center;'>Navigate to:</h4>", unsafe_allow_html=True)

    # Button to go to Historical Prices page
    if st.button("📈 Historical Prices"):
        st.session_state.page = "1_Historical_Prices"
        st.experimental_rerun()

    # Button to go to Compare Companies page
    if st.button("🏢 Compare Companies"):
        st.session_state.page = "2_Compare_Companies"
        st.experimental_rerun()

    # Button to go to Valuation Multiples page
    if st.button("💰 Valuation Multiples"):
        st.session_state.page = "3_Valuation_Multiples"
        st.experimental_rerun()

    st.write("---")
    st.success("👉 Use the buttons above to navigate!")