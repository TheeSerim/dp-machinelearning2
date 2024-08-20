import streamlit as st
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np
import pickle
import os
import pandas as pd
from streamlit_gsheets import GSheetsConnection


# Load the pickle data from the downloaded content
pickle_in = open("LGBM_tuned-2", 'rb')
model = pickle.load(pickle_in)

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")



def predict_loan(no_of_dependents,education_numeric,self_employed_numeric,income_annum,loan_amount,loan_term,residential_assets_value,commercial_assets_value,luxury_assets_value,bank_asset_value,capped_credit_score):
    input_data = np.array([[no_of_dependents,education_numeric,self_employed_numeric,income_annum,loan_amount,loan_term,residential_assets_value,commercial_assets_value,luxury_assets_value,bank_asset_value,capped_credit_score]]).astype(np.float32)
    prediction = model.predict(input_data)
    return float(prediction)

def run_loan():        
    st.title('💰 Loan Application Form 💰') 
    st.info('This App will help you determine if a client will be approved for a loan or rejected with their application')
    client_name = st.text_input("Enter your name")
    st.write(f"Hello, {client_name}!")

    # Text input
    

    #Number input for applicant's number of dependents
    no_of_dependents = st.number_input("Enter your number of dependents", min_value=0, max_value=5, value=0)
    st.write(f"The number of dependents entered is {no_of_dependents}")
    #st.write(f"Type of no_of_dependents: {type(no_of_dependents)}")

    education_options = ["Yes", "No"]
    education = st.selectbox("Is the applicant educated?", education_options)
    education_numeric = 1 if education == "Yes" else 0
    st.write(f"Selected: {education} (Converted to {education_numeric})")
    
    # Select box for self-employment
    self_employed_options = ["Yes", "No"]
    self_employed = st.selectbox("Is the applicant self-employed?", self_employed_options)
    self_employed_numeric = 1 if self_employed == "Yes" else 0
    st.write(f"Selected: {self_employed} (Converted to {self_employed_numeric})")
    

    #Number input for applicant's annual income
    income_annum = st.number_input("Enter your annual income", min_value=0, max_value=10000000, value=0)
    st.write(f"Your annual income entered is {income_annum}")

    #Number input for Loan_amount
    loan_amount = st.number_input("Enter a Loan_amount", min_value=0, max_value=10000000, value=0)
    st.write(f"The loan amount you would like to apply for is {loan_amount}")

    #Selectbox for loan term
    loan_term_options = list(range(2, 21, 2))
    loan_term = st.selectbox("Enter your loan term in months", loan_term_options, index=0)
    st.write(f"Your selected loan duration is {loan_term} months")

    #Number input for applicant's Residential asset values
    residential_assets_value = st.number_input("Enter your residential asset value", min_value=0, max_value=50000000, value=0)
    st.write(f"The residential asset value entered is {residential_assets_value}")

    #Number input for applicant's commercial asset values
    commercial_assets_value = st.number_input("Enter your commercial asset value", min_value=0, max_value=40000000, value=0)
    st.write(f"The commercial asset value entered is {commercial_assets_value}")

    #Number input for applicant's luxury asset values
    luxury_assets_value = st.number_input("Enter your luxury asset value", min_value=0, max_value=50000000, value=0)
    st.write(f"The luxury asset value entered is {luxury_assets_value}")

    #Number input for applicant's bank asset values
    bank_asset_value = st.number_input("Enter your bank asset value", min_value=0, max_value=50000000, value=0)
    st.write(f"The bank asset value entered is {bank_asset_value}")

    #Number input for Credit Score (Cibil_score)
    capped_credit_score = st.number_input("Enter your credit score", min_value=300, max_value=850, value=300)
    st.write(f"Your credit score entered is {capped_credit_score}")


   
    if st.button("Submit"):
        output = predict_loan(no_of_dependents,education_numeric,self_employed_numeric,income_annum,loan_amount,loan_term,residential_assets_value,commercial_assets_value,luxury_assets_value,bank_asset_value,capped_credit_score)
        st.success('The loan application outcome is {}'.format(output))
        if output == 0:
           st.error("Sorry, you are not eligible for a loan at this moment")
        else:
            st.success("Congratulations, you are eligible for a loan")
run_loan()



   
        
   








  


 

  
  

