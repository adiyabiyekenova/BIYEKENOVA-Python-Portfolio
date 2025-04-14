# 🧠 Custom Named Entity Recognition (NER) with spaCy

## 📌 Project Overview

This interactive web app lets users define their own **Named Entity Recognition (NER)** patterns using spaCy and instantly visualize the results on custom or uploaded text. Named Entity Recognition is a technique in Natural Language Processing (NLP) used to locate and classify named entities in text, such as names of people, organizations, dates, locations, etc.

spaCy provides a powerful tool for customizing NER pipelines using its **EntityRuler** component — this app puts that power into a user-friendly interface using **Streamlit**, allowing anyone to experiment with entity detection and annotation without writing code.

---

## ⚙️ Instructions

### ✅ Run the App Locally

1. Clone the repository:
   git clone https://github.com/your-username/custom-ner-spacy-app.git  
   cd custom-ner-spacy-app

2. Create a virtual environment (optional but recommended):
   python -m venv venv  
   source venv/bin/activate  (on Mac/Linux)  
   .\venv\Scripts\activate   (on Windows)

3. Install the required libraries:
   pip install -r requirements.txt

   Or manually:
   pip install streamlit spacy pandas  
   python -m spacy download en_core_web_sm

4. Run the app:
   streamlit run app.py

### 🌐 Deployed Version

🔗 Click here to view the deployed app: [your-streamlit-link](https://your-streamlit-cloud-url.streamlit.app)

---

## 🚀 App Features

### 1. Text Input Options
- Manually type or paste any text into the input box.
- Upload a `.txt` file.
- Choose from 3 example texts via dropdown.

### 2. Define Entity Patterns
- Use labeled input fields to specify:
  - Label (e.g., COMPANY, LOCATION, DATE)
  - Pattern (e.g., "Apple", "December 16, 1991")
- Add multiple pattern fields dynamically.
- View and delete added patterns anytime.

### 3. Visualize Entity Output
- Press "Analyze Text" to run spaCy’s NER pipeline with your custom EntityRuler.
- View detected entities inline using spaCy’s `displacy` visualizer.
- See a clean list of all extracted entity-label pairs below the visualization.

---

## 🧪 Example Usage

Example Pattern:  
Label: COMPANY  
Pattern: Apple

Example Text:  
"Apple is looking at buying U.K. startup for $1 billion."

Output:  
"Apple" is detected and labeled as COMPANY.

---

## 📚 References

- spaCy Documentation: https://spacy.io/usage  
- spaCy EntityRuler Guide: https://spacy.io/usage/rule-based-matching#entityruler  
- Streamlit Documentation: https://docs.streamlit.io/  
- DisplaCy Visualizer: https://spacy.io/usage/visualizers

---

## 🖼️ Visual Examples

### 🔧 App Interface
![App Interface](screenshots/interface.png)

### ✅ Annotated Entity Output
![Entity Output](screenshots/output.png)

> 📷 *Note: Replace these image paths with actual screenshots from your app stored in a `/screenshots` folder.*
