import streamlit as st
import pandas as pd
import numpy as np
import glob

st.set_page_config(layout="wide")

df = pd.read_parquet('data/nih_awards_no_abstract.parquet')

# define columns
filter_columns = st.columns([4, 4])

# Filter Columns
with filter_columns[0]:
    agencies = glob.glob('data/*/')
    agencies = [agency.split('\\')[1] for agency in agencies]
    agencies = sorted(agencies)
    agency = st.selectbox('Choose Agency', options=agencies)
    n_clusters = st.number_input('Choose Number of Clusters (3 to 29)', min_value=3, max_value=29, step=1)

if agency:
    # Read HTML file
    with open(f"data/{agency}/{agency}_{n_clusters}.html", "r") as f:
        html_content = f.read()

    # Display the HTML
    st.components.v1.html(html_content, height=1000, width=1300)