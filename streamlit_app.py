import streamlit as st
import joblib
import numpy as np
import pickle
import os
import pandas as pd


# Load the pickle data from the downloaded content
pickle_in = open("LGBM_tuned-2", 'rb')
model = pickle.load(pickle_in)


user_input = ["no_of_dependents","education","self_employed","income_annum","loan_amount","loan_term","residential_assets_value","commercial_assets_value","luxury_assets_value","bank_asset_value","capped_credit_score"]
Cat_features = ["education", "self_employed"]
#use this to converts categorical variables into a series of binary
#user_input = pd.get_dummies(user_input, user_input=Cat_features)
user_input = user_input.astype(np.float64)

def predict_loan(no_of_dependents,education,self_employed,income_annum,loan_amount,loan_term,residential_assets_value,commercial_assets_value,luxury_assets_value,bank_asset_value,capped_credit_score):
    input = np.array([[no_of_dependents,education,self_employed,income_annum,loan_amount,loan_term,residential_assets_value,commercial_assets_value,luxury_assets_value,bank_asset_value,capped_credit_score]]).astype(np.float64)
    data= pd.DataFrame([col],columns=columns)
    prediction = model.predict(input)
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
    
    #Select box for education
    #edu_options = ["Education = Yes", "Education = No"]
    #selected_option = st.selectbox("Choose an option", edu_options)
    #st.write(f"Selected: {selected_option}")

    # Select box for education
    edu_options = ["Yes", "No"]
    education = st.selectbox("Education", edu_options)
    # Map the selected option to a numerical value
    education_numeric = 1 if education == "Yes" else 0
    st.write(f"Selected: {education}")

    #Select box for self-employment
    self_employed = ["self_employ = Yes", "self_employ = No"]
    selected_option = st.selectbox("Choose an option", self_employed)
    self_employed_numeric = 1 if self_employed == "Yes" else 0
    st.write(f"Selected: {selected_option}")

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
    output = predict_loan('no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','residential_assets_value','commercial_assets_value','luxury_assets_value','bank_asset_value','capped_credit_score')
    st.success('The loan application outcome is {}'.formate(output))
    if output == 0:
       st.error("Sorry, you are not eligible for a loan at this moment")
    else:
       st.success("Congratulations you are eligible for a loan")


    
run_loan()



   
        
   








  #user_input = [[no_of_dep,edu_options,emp_options,annual_income,Loan_Amount,loan_term,res_assets,com_assets,lux_assets,bank_assets,Credit_score]]
 

   #Create a DataFrame for user inputs
   #user_data = pd.DataFrame({
   # "no_of_dep": [no_of_dependents],
   # "edu_options":[education],
   # "emp_options": [self_employed],
   #  "annual_income" : [income_annum],
   #  "Loan_Amount" : [loan_amount],
   # "loan_term" : [loan_term],
   #  "Credit_score" : [capped_credit_score],
   #  "res_assets" : [residential_assets_value],
   #  "com_assets" : [commercial_assets_value],
   #  "lux_assets" : [luxury_assets_value],
   #  "bank_assets" : [bank_asset_value]
   #})


 #columns = ['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','residential_assets_value','commercial_assets_value','luxury_assets_value','bank_asset_value','capped_credit_score']

  #Need to convert the categorica variables for self_employment and education to numerical values so that the model is able to comupute them
  #Categorical features

  #Cat_features = ["Self_Employed", "Education"]
  #use this to converts categorical variables into a series of binary
  #columns = pd.get_dummies(columns, columns=Cat_features)
  #columns = columns.astype(np.float32)


#def predict():
   #col= np.array([no_of_dependents,education,self_employed,income_annum,loan_amount,loan_term,residential_assets_value,commercial_assets_value,luxury_assets_value,bank_asset_value,capped_credit_score])
   #data= pd.DataFrame([col],columns=columns)

  #def predict():
    #col= np.array(['no_of_dep','edu_options','emp_options','annual_income','Loan_Amount','loan_term','Credit_score',
          #'res_assets','com_assets','lux_assets','bank_assets'])
   # data= pd.DataFrame([col],columns=columns)
          
  #prediction= model.predict(columns)[0]


 

  
  

