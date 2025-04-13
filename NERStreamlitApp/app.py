# Importing packages
import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
import json

# Load a spaCy model
nlp = spacy.load("en_core_web_sm")

# App title
st.title("🧠 Custom Named Entity Recognition (NER) with spaCy")
st.markdown("Use this app to define your own entities and see them in action.")

st.header("📄 Enter or Upload Text")
text_input = st.text_area("Enter your text here:", height=200)

uploaded_file = st.file_uploader("...or upload a .txt file", type=["txt"])
if uploaded_file:
    text_input = uploaded_file.read().decode("utf-8")

sample_texts = {
    "📱 Tech News": "Apple is looking at buying U.K. startup for $1 billion.",
    "🧬 Healthcare": "Pfizer and BioNTech announced a new vaccine for COVID-19.",
    "🚀 Space & Innovation": "NASA is planning a mission to Mars in 2028 with SpaceX."
}

# Dropdown to pick a sample
st.markdown("Or choose from one of our sample texts:")
sample_choice = st.selectbox("Choose a sample:", [""] + list(sample_texts.keys()))

if sample_choice:
    text_input = sample_texts[sample_choice]
    st.text_area("Sample text used:", value=text_input, height=200, key="sample_display")

        
st.header("🏷️ Define Custom Entity Patterns")

with st.expander("How to Define Patterns"):
    st.markdown("""
    - Use a list of dictionaries like in spaCy’s EntityRuler format.
    - Each pattern needs a `label` and a `pattern`. Example:
    ```json
    [
        {"label": "ORG", "pattern": "OpenAI"},
        {"label": "PRODUCT", "pattern": [{"LOWER": "iphone"}]}
    ]
    ```
    """)

pattern_json = st.text_area("Paste your custom patterns here (JSON format):", height=200)

# Process text with custom rules
if st.button("🔍 Analyze Text"):
    try:
        custom_patterns = json.loads(pattern_json)

        # Validate pattern format
        if not isinstance(custom_patterns, list):
            raise ValueError("Pattern JSON must be a list of dictionaries.")
        for pattern in custom_patterns:
            if not isinstance(pattern, dict):
                raise ValueError("Each pattern must be a dictionary.")
            if "label" not in pattern or "pattern" not in pattern:
                raise ValueError("Each dictionary must have 'label' and 'pattern' keys.")

        # Reset NLP pipeline and add custom ruler
        nlp = spacy.load("en_core_web_sm")  # Reload to clear old pipes
        ruler = nlp.add_pipe("entity_ruler", before="ner", config={"overwrite_ents": True})
        ruler.add_patterns(custom_patterns)

        doc = nlp(text_input)

        # Display results
        html = displacy.render(doc, style="ent", jupyter=False)
        st.markdown("### ✨ Detected Entities")
        st.components.v1.html(html, scrolling=True, height=300)

        # Show raw entities
        st.markdown("### 🗂️ Entity Details")
        for ent in doc.ents:
            st.write(f"• **{ent.text}** — *{ent.label_}*")

    except json.JSONDecodeError as e:
        st.error(f"JSON Error: {e}")
    except ValueError as ve:
        st.error(f"Validation Error: {ve}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")