import streamlit as st
import pandas as pd

# Title and description of the app
st.title("Basic Streamlit App")
st.write("""
    This app displays a sample dataset (Palmer's Penguins) and allows interactive filtering by species.
    You can select a species from the dropdown to view filtered data.
""")

# Load the penguins dataset from a CSV file located in the 'data' folder
df = pd.read_csv('data/penguins.csv')

# Display the first few rows of the dataset to the user
st.write("Sample DataFrame:")
st.dataframe(df.head())

# Create a dropdown menu for the user to select a species
species = st.selectbox('Select a species:', df['species'].unique())
# List unique species from the dataset

# Filter the dataset based on the selected species
filtered_df = df[df['species'] == species]
# Filter the DataFrame to show only the rows with the selected species

# Display the filtered data for the selected species
st.write(f"Data for {species} species:")
st.dataframe(filtered_df)
# Show the filtered DataFrame to the user