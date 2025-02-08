import streamlit as st
import pandas as pd
import os

# Title and description of the app
st.title("Basic Streamlit App")
st.write("""
    This app displays a sample dataset (Palmer's Penguins) and allows interactive filtering by species.
    You can select a species from the dropdown to view filtered data.
""")
df = pd.read_csv('data/penguins.csv')

st.write("Sample DataFrame:")
st.dataframe(df.head())

species = st.selectbox('Select a species:', df['species'].unique())

filtered_df = df[df['species'] == species]

st.write(f"Data for {species} species:")
st.dataframe(filtered_df)
