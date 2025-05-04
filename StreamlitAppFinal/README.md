# 📈 Investment Insights Streamlit App

## 📌 Project Overview

This interactive web application was developed as part of the *Elements of Computing II* class (Final Portfolio Update). Welcome to the **Investment Insights App** — a dynamic Streamlit dashboard that enables users to analyze public companies using real-time financial data. Whether you're a student, investor, or simply curious, this tool makes it easy to visualize and understand essential financial ratios.

---

## 🧠 Purpose of the App

### 🎯 Academic Context

This app serves as my final project for the *Elements of Computing II* course in Spring 2025. The goal was to demonstrate the culmination of my coding knowledge gained over the past year. I believe this app effectively showcases the range and quality of skills I’ve developed — from technical coding abilities to problem-solving and design thinking.

### 💡 Why I Built This App

As a Business Analytics major with a strong interest in both finance and technology, I wanted to create a project that bridges these two domains. This app was built to:

- Help users understand core financial health metrics  
- Visualize real-world financial data in an intuitive and engaging way  
- Encourage self-guided learning through interactive exploration  
- Strengthen my technical skills in API integration, data processing, and UI/UX design  
- Provide educational content that makes financial concepts accessible to everyone  

---

## 🖼️ App Interface – Main Page

The main page introduces users to the app’s features and provides a guided overview. Each section includes descriptions and links to specialized pages for deeper exploration.

### 📸 Screenshots:
- ![Screenshot 1](images/Screenshot1.png)
- ![Screenshot 2](images/Screenshot2.png)
- ![Screenshot 3](images/Screenshot3.png)
- ![Screenshot 4](images/Screenshot4.png)

At the bottom of the main page, users can easily navigate to three dedicated subpages offering more advanced functionality.

---

## 📂 App Structure 

The app is structured using Streamlit’s multipage feature for clarity and scalability:

- **`Home.py`** – Landing page with project overview and navigation  
- **`pages/Historical_Prices.py`** – Explore historical stock performance over a custom date range  
  - ![Screenshot 5](images/Screenshot5.png)
- **`pages/Compare_Companies.py`** – Compare two companies across multiple financial ratios  
  - ![Screenshot 6](images/Screenshot6.png)
- **`pages/Valuation_Multiples.py`** – Visualize valuation metrics like P/E, P/B, and dividend yield  
  - ![Screenshot 7](images/Screenshot7.png)

---

## ⚙️ How to Use the App

### ✅ Prerequisites

Ensure the following Python libraries are installed:

- `pandas`  
- `streamlit`  
- `yfinance`  
- `plotly`  
- `matplotlib`  
- `numpy`

### 🖥️ Running the App Locally

1. Clone the repository:  
   `git clone https://github.com/adiyabiyekenova/BIYEKENOVA-Python-Portfolio/StreamlitAppFinal.git`

2. Navigate to the app directory and run:  
   `streamlit run Home.py`

### 🌐 Deployed Version

Explore the deployed version of the app here:  
[🔗 Launch App](https://adiyabiyekenova-biyekenova-python-por-nerstreamlitappapp-3utzrp.streamlit.app/)

---

## ✨ Key Features

- 🔍 Search for public companies using stock tickers  
- 📊 View financial ratios in real time with interactive bar charts  
- 🆚 Compare companies side-by-side for better decision-making  
- 📈 Analyze historical stock performance over custom time ranges  
- 💰 Explore valuation multiples like P/E, P/B, and dividend yield  
- 📘 Learn about each metric through in-app educational descriptions  

---

## 🧑‍🎨 Design & User Experience

- Clean, intuitive layout with `set_page_config` and Streamlit’s responsive columns  
- Emoji-enhanced headings to make navigation friendly and fun  
- Optimized for both desktop and mobile viewing  
- Interactive Plotly charts for dynamic data exploration  
- Minimalist design with clear instructions and helpful visuals  

---

## 🛠️ Tools & Libraries Used

- **Streamlit** – Web application framework  
- **yFinance** – Real-time stock and financial data API  
- **Pandas** – Data analysis and manipulation  
- **NumPy** – Numerical computing  
- **Plotly Express** – Interactive visualizations  

---

## 📘 Skills Gained

- Integrating real-time financial data using APIs  
- Calculating financial metrics from raw data  
- Applying UI/UX principles in a Streamlit app  
- Creating advanced visualizations with Plotly  
- Structuring a multi-page application  
- Writing professional documentation and organizing code effectively  

---

## 📚 References & Learning Resources

These resources were incredibly helpful in building the app and deepening my understanding of Python and financial analysis:

- [📘 yFinance Python Library](https://pypi.org/project/yfinance/)  
- [📘 Streamlit Official Documentation](https://docs.streamlit.io/)  
- [📘 Plotly Express Overview](https://plotly.com/python/plotly-express/)  
- [📘 Investopedia: Financial Ratios Guide](https://www.investopedia.com/terms/f/financial-ratio.asp)  

---

## 🤝 Contribute

Feel free to open issues or contribute to the project.  
Thanks for checking out **Investment Insights**!
