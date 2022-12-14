# Import Libraries
import streamlit as st
import pandas as pd
from pathlib import Path
import numpy as np
from PIL import Image

# Set default page configuration
st.set_page_config(layout="wide", initial_sidebar_state='collapsed')

# Display  Image
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    image = Image.open('../Resources/Images/LoanApproved.png')
    st.image(image)
with col3:
    st.write(' ')

def colouredText(color1, color2, color3, content):
     st.markdown(f'<p style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});color:{color3};font-size:24px;border-radius:2%;">{content}</p>', unsafe_allow_html=True)

st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')

st.subheader('As part of this we project, we tried different machine learning algorithms to solve Risk Assessment binary classification problem. Below is the classification report for all the models we used. ')
st.write('\n')
st.write('\n')
st.write('\n')

# ------------------------------         Display results for Random Forest ------------------------------
colouredText('#ff80d5','#6699ff','#ffffff','Random Forest Learning Algorithm')
st.subheader('Classification Report')
data = {'precision': [0.99, 1.00],
        'recall': [1.0, 0.99],
        'f1-score': [0.99, 1.00],
        'support': [3829, 8669]}
df = pd.DataFrame(data, index=['Default (0)',
                               'Non Default (1)'])
st.dataframe(df)
st.write('\n')
st.image('../Resources/Images/ROC_RF.png')

# ------------------------------         Display results for Logistic Regression ------------------------------
colouredText('#6699ff','#ff80d5','#ffffff','Logistic Regression Learning Algorithm')
st.subheader('Classification Report')
data = {'precision': [0.92, 1.00],
        'recall': [1.0, 0.96],
        'f1-score': [0.96, 0.98],
        'support': [3829, 8669]}
  
# Creates pandas DataFrame.
df = pd.DataFrame(data, index=['Default (0)',
                               'Non Default (1)'])
st.dataframe(df)  
st.write('\n')
st.image('../Resources/Images/ROC_LR.png')

# ------------------------------         Display results for Decision Tree  ------------------------------
colouredText('#ff80d5','#6699ff','#ffffff','Decision Tree Learning Algorithm')
st.subheader('Classification Report')
data = {'precision': [0.99, 1.00],
        'recall': [1.0, 0.99],
        'f1-score': [0.99, 1.00],
        'support': [3829, 8669]}
  
# Creates pandas DataFrame.
df = pd.DataFrame(data, index=['Default (0)',
                               'Non Default (1)'])
st.dataframe(df)
st.write('\n')
st.image('../Resources/Images/ROC_DT.png')

# ------------------------------         Display results for Deep Learning ------------------------------
colouredText('#6699ff','#ff80d5','#ffffff','Deep Learning')
st.subheader('Classification Report')
data = {'precision': [0.70, 0.94],
        'recall': [0.85, 0.87],
        'f1-score': [0.76, 0.91],
        'support': [3189, 9309]}
  
# Creates pandas DataFrame.
df = pd.DataFrame(data, index=['Default (0)',
                               'Non Default (1)'])
st.dataframe(df)
st.write('\n')
st.image('../Resources/Images/ROC_DL.png')