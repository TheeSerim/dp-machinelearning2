import streamlit as st
import pickle

model = pickle.load(open('./TheeSerim/dp-machinelearning2/blob/master/model_loan2.pkl', 'rb'))
#https://github.com/TheeSerim/dp-machinelearning2/blob/master/model_loan2.pkl


st.title('🎈 Loan Application App')
st.info('This App is build to determine if a client will be approved or rejected for loan application')

# Text input
user_input = st.text_input("Enter your name")
st.write(f"Hello, {user_input}!")

# Number input for Loan_amount
Loan_Amount = st.number_input("Enter a Loan_amount", min_value=0, max_value=10000000, value=0)
st.write(f"The loan amount you would like to apply for is {Loan_Amount}")

# Select box for education
edu_options = ["Education = Yes", "Education = No"]
selected_option = st.selectbox("Choose an option", edu_options)
st.write(f"Selected: {selected_option}")

# Select box for self-employment
emp_options = ["self_employ = Yes", "self_employ = No"]
selected_option = st.selectbox("Choose an option", emp_options)
st.write(f"Selected: {selected_option}")

# Number input for Credit Score (Cibil_score)
Credit_score = st.number_input("Enter your Credit score", min_value=300, max_value=850, value=300)
st.write(f"Your credit score entered is {Credit_score}")

# Number input for applicant's annual income
annual_income = st.number_input("Enter your annual income", min_value=0, max_value=10000000, value=0)
st.write(f"Your annual income entered is {annual_income}")

# Number input for applicant's loan term
#loan_term = st.number_input("Enter your loan term", min_value=2, max_value=20, value=2)
#st.write(f"The duration of your loan entered is {loan_term}")

# Selectbox for loan term
loan_term_options = list(range(2, 21, 2))
loan_term = st.selectbox("Enter your loan term", loan_term_options, index=0)
st.write(f"The duration of your loan entered is {loan_term}")

# Number input for applicant's number of dependents
no_of_dep = st.number_input("Enter your number of dependents", min_value=0, max_value=5, value=0)
st.write(f"The number of dependents entered is {no_of_dep}")

# Number input for applicant's Residential asset values
res_assets = st.number_input("Enter your residential asset value", min_value=0, max_value=50000000, value=0)
st.write(f"The residential asset value entered is {res_assets}")

# Number input for applicant's commercial asset values
com_assets = st.number_input("Enter your commercial asset value", min_value=0, max_value=40000000, value=0)
st.write(f"The commercial asset value entered is {com_assets}")

# Number input for applicant's luxury asset values
lux_assets = st.number_input("Enter your luxury asset value", min_value=0, max_value=50000000, value=0)
st.write(f"The luxury asset value entered is {lux_assets}")

# Number input for applicant's bank asset values
bank_assets = st.number_input("Enter your bank asset value", min_value=0, max_value=50000000, value=0)
st.write(f"The bank asset value entered is {bank_assets}")


#Create a DataFrame for user inputs
user_data = pd.DataFrame({
  "No_of_dependents": [no_of_dependents],
  "Education":[education],
  "Self_Employed": [self_employed],
  "Annual_income" : [income_annum],
  "Loan_amount" : [loan_amount],
  "Loan_Duration" : [loan_term],
  "Credit_Score" : [cibil_score],
  "Residential_Assets" : [residential_assets_value],
  "Commercial_Assets" : [commercial_assets_value],
  "Luxury_Asset" : [luxury_assets_value],
  "Bank_Assets" : [bank_asset_value]
})

#Need to convert the categorica variables for self_employment and education to numerical values so that the model is able to comupute them
#Categorical features
Cat_features = ["Self_Employed", "Education"]
#use this to converts categorical variables into a series of binary
user_data = pd.get_dummies(user_data, columns=Cat_features)
user_data = user_data.astype(np.float32)


#Add the pre-trained model into the APP
prediction = model.predict(user_data)
Loan_Application_Status = prediction [0][0]
def main():
#Add what client will see on the APP screen
  if prediction > 1 :
      st.success("Congratulations you are eligible for a loan")
  else :
      st.error("Sorry you are not eligible at this moment")

if __name__ == "__main__":
  main()

  
  

