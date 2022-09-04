# Import Libraries
import streamlit as st
import pandas as pd
import pickle
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

st.write('\n')
st.write('\n')
st.write('\n')
# Import saved Model & Scaler
model = pickle.load(open('./../Model/model_rd.pkl', 'rb'))
scaler = pickle.load(open('./../Scaler/Scaler.pkl', 'rb'))

# Define function to create coloured text
def colouredText(color1, color2, color3, content):
     st.markdown(f'<p style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});color:{color3};font-size:24px;border-radius:2%;">{content}</p>', unsafe_allow_html=True)


# Define Industries list
industries = ['AccommodationAndFoodServices', 'AgricultureForestryAndFishing', 'ArtsAndRecreation', 'Construction', 'EducationAndTraining', 'ElectricityGasWaterAndWasteServices', 'HealthCareAndSocialAssistance', 'InformationMediaAndTelecommunications',
              'Manufacturing', 'OtherServices', 'ProfessionalScientificAndTechnicalServices', 'PublicAdministrationAndSafety', 'RentalHiringAndTrade', 'RetailTrade', 'ServicesSectors', 'TransportPostalAndWarehousing', 'WholesaleTrade']

# Generate dynamic variables
for industry in industries:
    dynamicvariable = industry
    globals()[dynamicvariable] = 0

# Initialize Form
with st.form("form2", clear_on_submit=False):
    user_loan_amount = st.text_input('Please enter amount you want to borrow. Minimum Loan Amount is 5000 AUD & Maximum Loan Amount is 100,000 AUD', value="")
    user_industry = st.selectbox('Select Industry', industries)
    globals()[user_industry] = 1
    user_zipCode = st.text_input('Please enter your office pincode', value="3000")
    user_businessHistory = st.text_input('How long you have been running this business', value="1")
    user_property = st.radio("Do you own a property ?", ('Yes', 'No'))
    user_otherLoan = st.radio("Do you have an existing loan?", ('Yes', 'No'))
    user_netCash = st.text_input("How much money you have in Bank?", value="")
    user_revenue = st.text_input("Please enter monthly revenue of your company", value="2000")
    user_taxReturn = st.text_input("How much tax you paid last year", value="")
    user_age = st.text_input('Please enter your age. Applicant must be 18 yrs old ', value="")

    

    applied = st.form_submit_button("Apply")
    # Once form is submitted 
    if applied:

        # Start of Validations
        if len(user_loan_amount) == 0 or int(user_loan_amount) < 5000 or int(user_loan_amount) > 100000:
            colouredText('#cc0000','#cc0000','#ffffff','Please enter the correct amount. Minimum Loan Amount is 5000 AUD & Maximum Loan Amount is 100,000 AUD')
            st.stop()
        if len(user_industry) == 0:
            colouredText('#cc0000','#cc0000','#ffffff','Please select Industry')            
            st.stop()
        if len(user_property) == 0:
            colouredText('#cc0000','#cc0000','#ffffff','Please enter if you own a property')           
            st.stop()
        if len(user_businessHistory) == 0 or int(user_businessHistory) < 1:
            colouredText('#cc0000','#cc0000','#ffffff','Please enter how long you have been running this business')            
            st.stop()
        if len(user_otherLoan) == 0:
            colouredText('#cc0000','#cc0000','#ffffff','Please select existing Loan')            
            st.stop()
        if len(user_netCash) == 0 or int(user_netCash) < 0:
            colouredText('#cc0000','#cc0000','#ffffff','Please enter cash in Bank')        
            st.stop()
        if len(user_revenue) == 0 or int(user_revenue) < 2000 :
            colouredText('#cc0000','#cc0000','#ffffff','Please enter monthly revenue of your company. Minimum montly revenue should be 2000 AUD')    
            st.stop()
        if len(user_taxReturn) == 0:
            colouredText('#cc0000','#cc0000','#ffffff','Please enter your last year tax returns')   
            st.stop()
        if len(user_age) == 0 or int(user_age) < 18:
            colouredText('#cc0000','#cc0000','#ffffff','Please enter your age')           
            st.stop()
        # End of validations

        if user_property =='Yes':
            user_property = 1
        else:
            user_property = 0

        if user_otherLoan =='Yes':
            user_otherLoan = 1
        else:
            user_otherLoan = 0
        
        # Create dataframe for model input
        X = pd.DataFrame([[int(user_revenue), int(user_loan_amount), int(user_businessHistory),  int(user_zipCode), user_property, user_otherLoan, int(user_netCash), int(user_age), int(user_taxReturn), AccommodationAndFoodServices, AgricultureForestryAndFishing, ArtsAndRecreation, Construction, EducationAndTraining, ElectricityGasWaterAndWasteServices, HealthCareAndSocialAssistance, InformationMediaAndTelecommunications, Manufacturing, OtherServices, ProfessionalScientificAndTechnicalServices, PublicAdministrationAndSafety, RentalHiringAndTrade, RetailTrade, ServicesSectors, TransportPostalAndWarehousing, WholesaleTrade]],
                                columns=['monthly_revenue', 'loanAmt', 'businessHistory', 'zipCode', 'hasProperty', 'otherLoan', 'cash', 'directorAge', 'taxReturn', 'AccommodationAndFoodServices', 'AgricultureForestryAndFishing', 'ArtsAndRecreation', 'Construction', 'EducationAndTraining', 'ElectricityGasWaterAndWasteServices', 'HealthCareAndSocialAssistance', 'InformationMediaAndTelecommunications', 'Manufacturing', 'OtherServices', 'ProfessionalScientificAndTechnicalServices', 'PublicAdministrationAndSafety', 'RentalHiringAndTrade', 'RetailTrade', 'ServicesSectors', 'TransportPostalAndWarehousing', 'WholesaleTrade'])

        # Scale dataframe
        X_scaled = scaler.transform(X)

        # Make Prediction
        predictions = model.predict(X_scaled)

        # Display Results
        if predictions[0] == 0:
            colouredText('#cc0000','#cc0000','#ffffff','Our model predicts that this loan has high chance of default')
            #st.write('Our model predicts that this loan has high chance of default')
        else:
            colouredText('#66ff99','#66ff99','#ffffff','Our model predicts that this loan has high chance of non-default')
            #st.write('Our model predicts that this loan has high chance of non-default')
