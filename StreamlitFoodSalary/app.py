import streamlit as st
from joblib import load

#load model joblib file
model = load('Salary_food_model.joblib')

#create Streamlit web app
st.title('Salary vs Food Expense Prediction')

#Add input field for income
income = st.number_input('Enter your income:')

#Add Prediction button
prediction_button = st.button('predict')

#Add prediction logic
if prediction_button:
    #input data into 2D array
    input_data = [[income/1000]]

    #Predict
    prediction = model.predict(input_data)[0]

    #display the Prediction
    st.write('Prediction food expense:', round(prediction*100, 2), 'บาท')