# Import Libraries
import streamlit as st
import pandas as pd
from pathlib import Path
import pickle
from PIL import Image

# Set default page configuration
st.set_page_config(layout="wide", initial_sidebar_state='collapsed')

# Display  Image
image = Image.open('./Images/LoanApproved.jpg')
st.image(image)

# Import save Model & Scaler
model = pickle.load(open('./../Model/Model.pkl', 'rb'))
scaler = pickle.load(open('./../Scaler/Scaler.pkl','rb'))

# Define list values
revenue = ['< 2000', '2000 - 5000', '5000-10000', ' > 10000']
operating_period = ['< 1 year', '1 year - 5 years', '5 years - 10 years', ' > 10 years']


st.write("Let's start by entering below details")

# Start of Form
with st.form("layer1", clear_on_submit=False):

    # user_revenue = st.multiselect(
    #     'Monthly Revenue of your company',
    #     revenue)
    # user_operating_period = st.number_input('How long you have been running this business')

    user_revenue = st.text_input('Monthly Revenue of your company',value="")
    user_operating_period = st.text_input('How long you have been running this business',value="")
    user_active_abn = st.radio("Is your Business Active",('Yes', 'No'))

    if len(user_revenue) == 0:
        st.write("Please provide Monthly Revenue of your company")
        error = st.form_submit_button("Submit")
        st.stop()
    
    if len(user_operating_period) == 0:
        st.write("Please provide how long you  have been running this business")
        error = st.form_submit_button("Submit")
        st.stop()

    if user_active_abn == 'No':
        st.write("Sorry, we can't proceed with your application")
        error = st.form_submit_button("Submit")
        st.stop()

    submitted = st.form_submit_button("Submit")
    if submitted:
        X = pd.DataFrame([[int(user_revenue), int(user_operating_period), 40190, 3, 0.2, 2911,0,0,186550,49,99180]],
        columns= ['monthly_revenue', 'min_operating_period', 'loanAmt', 'businessHistory', 'industry', 'zipCode', 'hasProperty', 'otherLoan', 'cash', 'directorAge', 'taxReturn'])
        st.write("Converted user input to X_test")
        st.write(X)
        predictions = model.predict(X)
        if predictions[0] == 0:
            st.write('Our model predicts that this loan will default')
        else:
            st.write('Our model predicts that this loan will not default')
