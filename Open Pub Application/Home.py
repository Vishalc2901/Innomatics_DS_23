import streamlit as st
import pandas as pd
import os

# absolute path to this file
file_dir = os.path.dirname(os.path.abspath(__file__))
# absolute path of directory_of_interest
dir_of_interest = os.path.join(file_dir, "data")
data_path = os.path.join(dir_of_interest, "pub_clean.csv")
df=pd.read_csv(data_path)

st.set_page_config(page_title="Home")

st.title(":red[Hello!] :blue[I am Vishal]")
st.header("I am a Data Science intern at  Innomatics Research Labs")

st.title(":red[Open Nearest Pub App]")

st.write(
    """
- ✔️ Go to Nearest pub page for finding 5 nearest pubs
- ✔️ Go to Pub location Page for finding pub location
"""
)

st.subheader('Dataset')
st.dataframe(df)

st.subheader('Covariance in dataset')
st.dataframe(df.cov())

st.subheader('Satistical Analysis')    
st.dataframe(df.describe())

st.subheader('Correlation')  
st.dataframe(df.corr())