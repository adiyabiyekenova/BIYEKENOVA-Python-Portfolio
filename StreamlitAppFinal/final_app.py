import streamlit as st

st.set_page_config(page_title="Investment Insights App", layout="wide")

# Optional: Add logo or header image
# st.image("your_logo.png", width=200)

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

    # Call to action
    st.success("👉 Use the sidebar to navigate between tools!")
    
    # Add a button with animation
    if st.button("🚀 Go to Dashboard"):
        st.toast("Navigation is on the left sidebar!", icon="📂")
        st.markdown("### Navigate using the sidebar menu ➡️")

st.write("---")
st.caption("Made with ❤️ using Streamlit • Designed for finance pros")
