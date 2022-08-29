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

# Import save Model & Scaler
model = pickle.load(open('./../Model/Model.pkl', 'rb'))
scaler = pickle.load(open('./../Scaler/Scaler.pkl','rb'))

# Define list values
revenue = ['< 2000', '2000 - 5000', '5000-10000', ' > 10000']
operating_period = ['< 1 year', '1 year - 5 years', '5 years - 10 years', ' > 10 years']
industryDict = {"Construction":1,"Health":2,"Science":3}


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
        st.text("Please provide Monthly Revenue of your company")
        error = st.form_submit_button("Submit")
        st.stop()
    
    if len(user_operating_period) == 0:
        st.write("Please provide how long you  have been running this business")
        error = st.form_submit_button("Submit")
        st.stop()

    if user_active_abn == 'No':
        st.text("Sorry, we can't proceed with your application")
        error = st.form_submit_button("Submit")
        st.stop()

    submitted = st.form_submit_button("Submit")

with st.form("layer2", clear_on_submit=False):
    user_loan_amount = st.text_input('Please enter amount you want to borrow. Minimum Loan Amount is 5000 AUD',value="")
    user_industry = st.selectbox('Select Industry',industryDict.keys())
    user_zipCode = st.text_input('Please enter your office pincode',value="3000")
    user_property = st.radio("Do you own a property ?",('Yes', 'No'))
    user_otherLoan = st.radio("Do you have an existing loan?",('Yes', 'No'))
    user_netCash = st.text_input("How much money you have in Bank?",value="")
    user_taxReturn = st.text_input("How much money you have in Bank?",value="")
    user_age = st.text_input('Please enter your age',value="")
    if len(user_loan_amount) == 0 or int(user_loan_amount) <= 5000 :
        st.write("Please enter amount you want to borrow")
        error = st.form_submit_button("Submit")
        st.stop()   
    if len(user_industry) == 0 :
        st.write("Please select Industry")
        error = st.form_submit_button("Submit")
        st.stop()
    submitted = st.form_submit_button("Submit")
    if submitted:
        X = pd.DataFrame([[int(user_revenue), int(user_operating_period), int(user_loan_amount), 3, industryDict.get(user_industry), int(user_zipCode),0,0,186550,49,99180]],
            columns= ['monthly_revenue', 'min_operating_period', 'loanAmt', 'businessHistory', 'industry', 'zipCode', 'hasProperty', 'otherLoan', 'cash', 'directorAge', 'taxReturn'])
        st.write("Converted user input to X_test")
        st.write(X)
        predictions = model.predict(X)
        if predictions[0] == 0:
            st.write('Our model predicts that this loan will default')
        else:
            st.write('Our model predicts that this loan will not default')