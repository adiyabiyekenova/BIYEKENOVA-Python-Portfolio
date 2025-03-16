## 📝 Project Overview
This project is part of the *Elements of Computing II Portfolio Update 2* and demonstrates the principles of **tidy data** using Python. The primary goal is to clean, reshape, and visualize the dataset to ensure that:
- ✅ Each variable has its own column.
- ✅ Each observation forms its own row.
- ✅ Each type of observational unit is stored in a separate table.

By applying these principles, we ensure that the data is structured in a way that facilitates analysis and visualization.

### Project Structure
The project consists of three main parts:
1. **Tidying the Data** - Cleaning and reshaping the dataset to follow tidy data principles.
2. **Visualizing the Data** - Creating visualizations to explore trends and insights.
3. **Pivot Tables** - Summarizing the data using pivot tables for deeper analysis.

The Jupyter notebook includes comments for the code and markdown cells that explain findings and guide you through the steps.

---

## ⚙️ Instructions

### 📌 Prerequisites
To run this project, you will need the following dependencies:
pip install pandas matplotlib seaborn jupyterlab


### 🚀 Running the Notebook
1. **Clone this repository:**
   
bash
   git clone https://github.com/adiyabiyekenova/TidyData-Project.git
   cd TidyData-Project

2. **Launch Jupyter Notebook:**
   
bash
   jupyter lab

3. **Open and run** tidy_data_project.ipynb to execute data cleaning and visualizations.

---

## 📂 Dataset Description
The dataset used in this project represents **Federal R&D Budgets** over multiple years and their relationship with GDP.

- 📌 **Source:** [Adapted from Github](https://github.com/rfordatascience/tidytuesday/tree/main/data/2019/2019-02-12)

The data comes directly from the *American Association for the Advancement of Science Historical Trends*. It tracks spending on research and development by each governmental agency from 1976 to 2017, along with corresponding GDP figures.

### Why Analyze This Data?
1. To see which departments are spending significantly on research and development.
2. To understand how spending across different agencies and overall has changed over time.
3. To examine how research and development spending relates to GDP growth, and whether the government has increased or decreased spending on R&D relative to the economy.

### Why Use This Data for Coding?
1. The dataset contains around 600 observations, which provides enough variety for interesting insights but is still manageable for analysis.
2. It has 4 variables, allowing us to explore different relationships and trends with a single dataset.
3. While the initial CSV file is untidy, it is not overly complex, making it an ideal candidate for cleaning and reshaping exercises.

---

## 📊 Conclusions and Visual Examples
This project includes multiple visualizations to help analyze the dataset:

1. 📈 **R&D Budget Trends as % of GDP** - A line chart showing how department-wise budgets compare to GDP over time.
   !(https://github.com/adiyabiyekenova/BIYEKENOVA-Python-Portfolio/blob/main/TidyData-Project/visualization1.png)

2. 📊 **Total R&D Spending vs. GDP** - A dual-axis plot comparing total R&D spending with GDP growth.
   ![Visualization Example](http://github.com/adiyabiyekenova/BIYEKENOVA-Python-Portfolio/blob/main/TidyData-Project/visualization2.png)

### Key Findings:
- Both **R&D spending** and **GDP** have grown significantly over the years, but GDP has grown at a much larger pace than R&D spending.
- Departments with the largest budgets—such as the **Department of Defense (DOD)**, **Department of Energy (DOE)**, **NASA (National Aeronautics and Space Administration)**, **Department of Health and Human Services (HHS)**, and **National Institutes of Health (NIH)**—stand out due to their consistently high spending levels.
- The trend suggests that while the government continues to allocate substantial funds to R&D, the relative share of R&D spending in the overall economy has decreased.

---

## 🔧 Tools and Libraries Used:
- **pandas** - For data manipulation and cleaning.
- **matplotlib** - For creating static, animated, and interactive visualizations.
- **seaborn** - For statistical data visualization.

### Skills Gained:
- Mastery of **tidy data principles**, ensuring data is in a clean, structured format for analysis.
- Proficiency in **data cleaning** techniques such as reshaping data and handling missing values.
- **Data visualization** skills to communicate insights clearly through charts and graphs.
- Experience with **pivot tables** for summarizing and analyzing large datasets.

---

## 🔗 References
- 📄 [Tidy Data Paper by Hadley Wickham](https://vita.had.co.nz/papers/tidy-data.pdf)
- 🗂 [Tidy Data Cheat Sheet](https://www.rstudio.com/resources/cheatsheets/)

For any questions or contributions, feel free to submit an issue or pull request!

---

🚀 **Happy Coding!**
