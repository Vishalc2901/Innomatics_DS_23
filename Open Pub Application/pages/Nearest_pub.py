import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import os
import Home

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "data")
DATA_PATH = os.path.join(dir_of_interest, "pub_clean.csv")
df=pd.read_csv(DATA_PATH)

st.set_page_config(page_title="Nearest Pubs")

lati =st.number_input('Latitude')
lon =st.number_input('Longitude')
new_df=df[['latitude','longitude']]
inputs=np.array([lati,lon])
distance=np.sqrt(np.sum((inputs-new_df)**2, axis=1))
n = 5
nearest_neighbor = distance.argsort()[:n]

if st.button('Find'):
    st.subheader(":red[Here are 5 nearest pubs for you : ]")
    st.map(df.iloc[nearest_neighbor])
    st.dataframe(df.iloc[nearest_neighbor])