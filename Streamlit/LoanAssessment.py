# Import Libraries
import streamlit as st
import pandas as pd
from pathlib import Path
import pickle

# Set default page configuration
st.set_page_config(layout="wide", initial_sidebar_state='collapsed')

# Display  Image
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image('./Images/LoanApproved.jpg')
with col3:
    st.write(' ')

#st.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)
st.write('This page will provide stats about the model')