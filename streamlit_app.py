import streamlit as st
import pickle

#model = pickle.load(open('./master/model_loan2.pkl', 'rb'))
#https://github.com/TheeSerim/dp-machinelearning2/blob/master/model_loan2.pkl

st.title('🎈 Loan Application App')

st.info('This App is build to determine if a client will be approved or rejected for loan application')

# Text input
user_input = st.text_input("Enter your name")
st.write(f"Hello, {user_input}!")

# Number input for Loan_amount
Loan Amount = st.number_input("Enter a Loan_amount", min_value=0, max_value=10000000, value=0)
st.write(f"The number you entered is {Loan Amount}")

# Select box for education
options = ["Education = Yes", "Education = No"]
selected_option = st.selectbox("Choose an option", options)
st.write(f"Selected: {selected_option}")

# Number input for Credit Score (Cibil_score)
number = st.number_input("Enter your Credit score", min_value=0, max_value=10000000, value=0)
st.write(f"The number you entered is {number}")


