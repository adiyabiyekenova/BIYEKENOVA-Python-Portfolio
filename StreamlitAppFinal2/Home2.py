# Import the Streamlit library 
import streamlit as st

# Set up the basic configuration of the Streamlit page
# Set the name of the tab in the browser using page_title
# Use the full screen width with layout='wide'
st.set_page_config(page_title="Stock Insights App", layout="wide")

# Add a main title to the page using HTML styling to center it and make it large
st.markdown("<h1 style='text-align: center;'>📊 Investment Insights App</h1>", unsafe_allow_html=True)

# Add a subtitle just below the main title (also styled in HTML and centered)
st.markdown("<h4 style='text-align: center; color: grey;'>Visualize, Compare, and Learn About Stocks Like a Pro</h4>", unsafe_allow_html=True)

# Add a horizontal line as a visual separator
st.write("---")

# Create a layout with three columns: a narrow one on the left, a wide one in the center, and another narrow one on the right
# This centers the main content visually
col1, col2, col3 = st.columns([1, 3, 1])

# Place all the main content inside the center column
with col2:
    # Display an image at the top 
    st.image("https://cdn-icons-png.flaticon.com/512/2463/2463510.png", width=150)

    # Add a detailed welcome message and app description using Markdown
    # This includes emoji and line breaks to make it easy to read
    st.markdown("""
    Welcome to the **Investment Insights App** – your all-in-one toolkit to learn about and analyze stocks!  
    Whether you're a seasoned investor or just curious about the stock market, this app will help you:
    - 📈 **View historical stock prices** to see how a company performed over time  
    - 🏢 **Compare different companies** using important financial metrics  
    - 💰 **Explore valuation multiples** to understand how stocks are priced  

    This app is perfect for students, beginners, and curious minds who want to explore how businesses grow and how investors make smart decisions.

    ---

    ### 💡 What’s a Stock? 
    A **stock** is like owning a tiny piece of a company.  
    Imagine if your favorite lemonade stand said, “Hey, you can own a piece of our business!”  
    If you buy a stock, it means you believe that the lemonade stand will do well—and if it does, your piece becomes more valuable! 🍋📈

    Stocks let people **invest** in businesses and grow their money as those businesses grow.

    You can:
    - Watch prices go up and down 🎢
    - See how one company stacks up against another 
    - Learn how the world of money really works 🧠💼

    ---

    ### 🔍 What Each Page Does:

    **📈 Historical Prices**  
    Dive into a company’s stock price history and spot important trends and patterns over time. This page is perfect for visual learners who love charts and graphs. Simply choose any publicly traded company, select a time period, and watch how the stock price has moved over time. It’s a great way to understand market momentum and how companies react to big events.

    **🏢 Compare Companies**  
    Ever wondered how two companies stack up against each other? This tool lets you compare them side-by-side using key metrics like Market Capitalization, Price-to-Earnings (P/E) Ratio, and Dividend Yield. Each metric is explained right on the page, so you’ll never feel lost. It’s a fun and easy way to decide which company is leading the race!

    **💰 Valuation Multiples**  
    This section helps you understand how investors decide whether a stock is cheap, expensive, or just right. You can explore a variety of valuation multiples—like Return on Equity, Asset Turnover, Debt-to-Equity Ratio—and see how different companies compare using clean, interactive charts. Not sure what a multiple means? No worries! Each one is explained so you can learn as you explore.

    ---

    ### 🧩 Interactive Learning:
    - Try selecting your favorite brand (like Apple or Nike) and see how it performs!
    - Mix and match companies to compare them like a fun trading card game!

    Let’s make learning finance exciting and hands-on.

    ---
    """)

    # Section title to guide users to choose where they want to go next (styled in HTML and centered)
    st.markdown("<h4 style='text-align: center;'>🚀 Choose Where to Begin:</h4>", unsafe_allow_html=True)
    st.markdown("After you press a button, **click on the link that appears** to navigate to the page you chose.")

    # Create buttons for the user to navigate to different pages
    # When clicked, the link to the page appears 
    if st.button("📈 Historical Prices"):
        st.page_link("pages/Historical.py")
        
    if st.button("🏢 Compare Companies"):
        st.page_link("pages/Compare.py")
        
    if st.button("💰 Valuation Multiples"):
        st.page_link("pages/Valuation.py")

    # Add another horizontal line for separation
    st.write("---")

    # Add a green success box to encourage clicking the buttons above using .success
    st.success("👉 Use the buttons above to explore the world of stocks!")