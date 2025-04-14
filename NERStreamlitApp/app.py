# Section 0: Logistics
# Importing all necessary libraries
import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
import pandas as pd

# Load English model from spaCy
nlp = spacy.load("en_core_web_sm")

# Section 1: Initial setup and design of the app
# Setting the app title 
st.title("🧠 Custom Named Entity Recognition (NER) with spaCy")
st.write("This app lets you define your own custom entities and see them in your text.")
# Setting a section where users can type their own text or upload a file
st.header("📄 Enter or Upload Text")
# Text box for manual input
text_input = st.text_area("Enter your text here:", height=300)
# Box to upload a .txt file 
uploaded_file = st.file_uploader("...or upload a .txt file", type=["txt"])
# If the file was uploaded... 
if uploaded_file:
    text_input = uploaded_file.read().decode("utf-8") #... we read and decode the text file 
    st.success("Text file uploaded successfully!") # Display the success message 
# Make a dictionary of pre-written sample texts (examples from the assignment and my own)
sample_texts = {
    "📈 Stock Market Update": "Helmerich & Payne (HP) saw its stock rise by 1.5%, fueled by optimistic forecasts in the Energy Equipment & Services sector. In contrast, Check-Cap (CHEK) faced a decline of 2.3% following its announcement of increased costs related to supply chain disruptions. Meanwhile, Vallon Pharmaceuticals (VLON) gained 0.8% after strong quarterly earnings, outperforming its peers in the Biotechnology space. Sequans Communications (SQNS) also recorded a modest increase of 0.5%, reflecting investors' confidence in its ability to navigate challenges in the Semiconductors & Semiconductor Equipment industry.",
    "🌱 EU Renewable Energy Funding": "In July 2022, the European Union approved a $1.2 billion aid package for renewable energy projects in Spain and Portugal. The funding was announced by Ursula von der Leyen, President of the European Commission, during a summit held in Brussels. The initiative aims to support solar and wind energy startups, particularly in regions like Andalusia and Alentejo. Major companies like Iberdrola and EDP Renewables are expected to benefit from the subsidies, which align with the EU’s Green Deal goals for 2030.",
    "🇰🇿 Kazakhstan Independence": "Kazakhstan declared its independence from the Soviet Union on December 16, 1991. Nursultan Nazarbayev became the country’s first president and served until 2019. The capital city, previously known as Astana, was renamed Nur-Sultan in 2019 in his honor, though it later reverted back to Astana in 2022. Almaty, the largest city, was the former capital and remains a cultural and economic center of Kazakhstan."
}
# Dropdown to pick a sample
st.write("Or choose from one of the sample texts:")
# Create a selectbox with an option of an empty string "", all the items from the dictionary converted to a list 
# The selected value will be stored in the variable sample_choice 
sample_choice = st.selectbox("Choose a sample:", [""] + list(sample_texts)) 
# If a sample is selected... 
if sample_choice:
    text_input = sample_texts[sample_choice] #fill the input box with that text
    st.text_area("Sample text used:", value=text_input, height=300, key="sample_display") #Display the chosen text from the sample choices

# Section 2: The user defines Entity Patterns 
# Create a title section in the app 
st.header("🏷️ Define Entity Pattern")
# If patterns doesn't exist yet, create it as an empty list to hold all custom entity patterns the user adds
if "patterns" not in st.session_state:
    st.session_state.patterns = []
# If pattern fields doesn't exist yet, initialize it to 1 to keep track of how many input fields for patterns there are 
if "pattern_fields" not in st.session_state:
    st.session_state.pattern_fields = 1  # Start with one pattern field
# Allow the user to add more than one input field dynamically through the button 
# If the user clicks the button, increase the number of pattern input sections shown by one 
if st.button("➕ Add More Pattern Fields"):
    st.session_state.pattern_fields += 1
# Loop through the number of pattern fields that the user has entered (the number is the number of patterns the user added)
for i in range(st.session_state.pattern_fields):
    # Show each pattern that was added
    st.write(f"Pattern {i + 1}")
    # Input field for the entity label with the number of the pattern being added
    label = st.text_input(f"Entity label {i + 1}", key=f"label_{i}")
    # Input field for the text pattern
    pattern = st.text_input(f"Text pattern to match {i + 1}", key=f"pattern_{i}")
    # When the user clicks the "Add Pattern" button
    if st.button(f"Add Pattern {i + 1}", key=f"add_pattern_{i}"):
        # ...check if both label and pattern are filled
        if label and pattern:
            # Add the pattern to session state with the label in uppercase and a success message 
            st.session_state.patterns.append({
                "label": label.strip().upper(),
                "pattern": pattern.strip()
            })
            st.success(f"Pattern added: {pattern.strip()} as {label.strip().upper()}")
        else:
            # If either is missing, show an error message
            st.error("Please enter both a label and a pattern.")

# Display the list of all added patterns and allow deleting them with a button
# If there are patterns that were added in session state
if st.session_state.patterns:
    st.write("Current Entity Patterns")
    # Loop through the list of patterns and display them
    for x, p in enumerate(st.session_state.patterns):
        # Create two columns for the list of patterns and display item
        cols = st.columns([4, 1])
        with cols[0]:
            # Show the pattern and label 
            st.write(f"{p['pattern']}: {p['label']}")
        with cols[1]:
            # Add a delete button next to each pattern
            # If the delete button is pressed, remove the selected pattern from the session
            if st.button("🗑️", key=f"delete_{x}"):
                st.session_state.patterns.pop(x)
                # Rerun the app so that changes are reflected immediately
                st.rerun()
                
# Section 3: Analyze text with added patterns
#When the user clicks the "Analyze Text" button ...
if st.button("🔍 Analyze Text"):
    #check the input text (either user input or sample text) to analyze 
    if not text_input.strip():
        st.error("Please enter or upload some text first.")
    else:
        # If the entity ruler is already added, remove it first to avoid conflicts
        if "entity_ruler" in nlp.pipe_names:
            nlp.remove_pipe("entity_ruler")
        # Add a new entity ruler before the default NER pipeline 
        ruler = nlp.add_pipe("entity_ruler", before="ner")
        # add the custom patterns into the entity ruler 
        ruler.add_patterns(st.session_state.patterns)
        # Process the input text using spaCy 
        doc = nlp(text_input)
        # Display entities using displacy 
        st.write("Detected Entities")
        html = displacy.render(doc, style="ent", jupyter=False)
        st.components.v1.html(html, scrolling=True, height=300)
        # List out each detected entity with its label
        st.write("🗂️ Entity Details")
        if doc.ents:
            for ent in doc.ents:
                st.write(f"{ent.text}: {ent.label_}")
        else:
            st.info("No entities found with the current patterns.")