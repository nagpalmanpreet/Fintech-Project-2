# Import Libraries
import streamlit as st
import webbrowser
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

st.write('\n')
st.write('\n')
st.write('\n')

# Define dropdown values
revenue = ('Less than 2000', '2000 - 5000',
           '5000-10000', ' Greater than 10000')
operating_period = ('Less than a year', '1 year - 5 years',
                    '5 years - 10 years', ' More than 10 years')

# Define function to create coloured text
def colouredText(color1, color2, color3, content):
     st.markdown(f'<p style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});color:{color3};font-size:24px;border-radius:2%;">{content}</p>', unsafe_allow_html=True)


# Start of Form
with st.form("form1", clear_on_submit=False):

    user_revenue = st.selectbox('Monthly Revenue of your company', revenue)
    user_operating_period = st.selectbox(
        'How long you have been running this business', operating_period)
    user_active_abn = st.radio("Is your Business Active", ('Yes', 'No'))


    submitted = st.form_submit_button("Submit")

if submitted:
    # Ineligible application
    if user_revenue == 'Less than 2000' or user_operating_period == 'Less than a year' or user_active_abn == 'No':        
        if user_revenue == 'Less than 2000':
            error_message = 'Monthly Revenue must be greater than 2000 AUD for loan eligibility. '
        elif user_operating_period == 'Less than a year':
            error_message = 'Your business should be atleast 1 year old'
        else:
            error_message = "You don't have an active business"
        message = 'Sorry, you are not eligible for loan. ' + error_message
        colouredText('#cc0000','#cc0000','#ffffff', message)
        st.stop()
    else:
        #Jump to next page
        url = 'http://localhost:8501/Page2'
        webbrowser.open_new_tab(url)

