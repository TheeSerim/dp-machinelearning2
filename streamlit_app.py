import streamlit as st
import joblib
import numpy as np
import pickle
import os
import pandas as pd



# Load the pickle data from the downloaded content
pickle_in = open("LGBM_tuned-2", 'rb')
model = pickle.load(pickle_in)


def run_loan():          
    st.title(' £ 💰 Loan Application Form £ 💰') 
    st.info('This App is build to determine if a client will be approved or rejected for loan application')
    st.text_input("Enter your name")
    st.write(f"Hello, {user_input}!")

    # Text input
    # Number input for Loan_amount
    Loan_Amount = st.number_input("Enter a Loan_amount", min_value=0, max_value=10000000, value=0)
    st.write(f"The loan amount you would like to apply for is {Loan_Amount}")

    #Select box for education
    edu_options = ["Education = Yes", "Education = No"]
    selected_option = st.selectbox("Choose an option", edu_options)
    st.write(f"Selected: {selected_option}")

    #Select box for self-employment
    emp_options = ["self_employ = Yes", "self_employ = No"]
    selected_option = st.selectbox("Choose an option", emp_options)
    st.write(f"Selected: {selected_option}")

    #Number input for Credit Score (Cibil_score)
    Credit_score = st.number_input("Enter your Credit score", min_value=300, max_value=850, value=300)
    st.write(f"Your credit score entered is {Credit_score}")

    #Number input for applicant's annual income
    annual_income = st.number_input("Enter your annual income", min_value=0, max_value=10000000, value=0)
    st.write(f"Your annual income entered is {annual_income}")


    #Selectbox for loan term
    loan_term_options = list(range(2, 21, 2))
    loan_term = st.selectbox("Enter your loan term", loan_term_options, index=0)
    st.write(f"The duration of your loan entered is {loan_term}")

    #Number input for applicant's number of dependents
    no_of_dep = st.number_input("Enter your number of dependents", min_value=0, max_value=5, value=0)
    st.write(f"The number of dependents entered is {no_of_dep}")

    #Number input for applicant's Residential asset values
    res_assets = st.number_input("Enter your residential asset value", min_value=0, max_value=50000000, value=0)
    st.write(f"The residential asset value entered is {res_assets}")

    #Number input for applicant's commercial asset values
    com_assets = st.number_input("Enter your commercial asset value", min_value=0, max_value=40000000, value=0)
    st.write(f"The commercial asset value entered is {com_assets}")

    #Number input for applicant's luxury asset values
    lux_assets = st.number_input("Enter your luxury asset value", min_value=0, max_value=50000000, value=0)
    st.write(f"The luxury asset value entered is {lux_assets}")

    #Number input for applicant's bank asset values
    bank_assets = st.number_input("Enter your bank asset value", min_value=0, max_value=50000000, value=0)
    st.write(f"The bank asset value entered is {bank_assets}")

if st.button("Submit"):

   user_input = [[no_of_dep,edu_options,emp_options,annual_income,Loan_Amount,loan_term,
          res_assets,com_assets,lux_assets,bank_assets,Credit_score]]
   print(user_input)
   #Create a data frame for the user inputs
   user_input_df = pd.DataFrame(user_input)

   prediction = model.predict(user_input_df.values)
   lc = [str(i) for i in prediction]
   ans = int("".join(lc))
if ans == 0:
   st.error("Sorry, you are not eligible for a loan at this moment")
  else:
     st.success("Congratulations you are eligible for a loan")

run_loan()
 


   #Create a DataFrame for user inputs
   #user_data = pd.DataFrame({
   # "no_of_dep": [no_of_dependents],
   # "edu_options":[education],
   # "emp_options": [self_employed],
   #  "annual_income" : [income_annum],
   #  "Loan_Amount" : [loan_amount],
   # "loan_term" : [loan_term],
   #  "Credit_score" : [cibil_score],
   #  "res_assets" : [residential_assets_value],
   #  "com_assets" : [commercial_assets_value],
   #  "lux_assets" : [luxury_assets_value],
   #  "bank_assets" : [bank_asset_value]
   #})



  #Need to convert the categorica variables for self_employment and education to numerical values so that the model is able to comupute them
  #Categorical features

  #Cat_features = ["Self_Employed", "Education"]
  #use this to converts categorical variables into a series of binary
  #columns = pd.get_dummies(columns, columns=Cat_features)
  #columns = columns.astype(np.float32)



  #def predict():
    #col= np.array(['no_of_dep','edu_options','emp_options','annual_income','Loan_Amount','loan_term','Credit_score',
          #'res_assets','com_assets','lux_assets','bank_assets'])
   # data= pd.DataFrame([col],columns=columns)
          
  #prediction= model.predict(columns)[0]


 

  
  

