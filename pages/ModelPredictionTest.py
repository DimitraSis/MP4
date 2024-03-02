#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from joblib import load
import pandas as pd

# Load your trained model
model = load('C:\\DAT1E22Bxd\\3rd semester\\MP4\\decision_tree_model.pkl')

# Function to predict attrition
def predict_attrition(user_data):
    data = pd.DataFrame(user_data, index=[0])
    prediction = model.predict(data)
    probability = model.predict_proba(data)[0][1]
    return prediction[0], probability

# Streamlit app layout
st.title('Employee Attrition Prediction')

# Numeric inputs
age = st.number_input('Age', min_value=18, max_value=65, value=35)
total_working_years = st.number_input('Total Working Years', min_value=0, max_value=50, value=10)
job_level = st.number_input('Job Level', min_value=1, max_value=5, value=1)
years_in_current_role = st.number_input('Years In Current Role', min_value=0, max_value=40, value=1)
monthly_income = st.number_input('Monthly Income', min_value=1000, max_value=20000, value=5000)
years_with_curr_manager = st.number_input('Years With Current Manager', min_value=0, max_value=40, value=1)
years_at_company = st.number_input('Years At Company', min_value=0, max_value=40, value=1)
stock_option_level = st.number_input('Stock Option Level', min_value=0, max_value=3, value=0)

# Dropdowns for categorical variables (example for Job Role and Marital Status)
job_role_sales_representative = st.selectbox('Job Role', ['Sales Representative', 'Other']) == 'Sales Representative'
marital_status_single = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced']) == 'Single'

# Radio buttons for binary choices (example for OverTime)
overtime = st.radio('OverTime', ['Yes', 'No'])
overtime_yes = overtime == 'Yes'
overtime_no = overtime == 'No'

# Sliders for satisfaction levels and other ordinal data
job_satisfaction = st.slider('Job Satisfaction', 1, 4, 2)
job_involvement = st.slider('Job Involvement', 1, 4, 2)
environment_satisfaction = st.slider('Environment Satisfaction', 1, 4, 2)
business_travel_frequent = st.radio('Business Travel Frequency', ['Never', 'Rarely', 'Frequently']) == 'Frequently'

# Collect inputs in a dictionary
user_data = {
    'OverTime_Yes': [int(overtime_yes)],
    'OverTime_No': [int(overtime_no)],
    'MaritalStatus_Single': [int(marital_status_single)],
    'TotalWorkingYears': [total_working_years],
    'JobLevel': [job_level],
    'YearsInCurrentRole': [years_in_current_role],
    'MonthlyIncome': [monthly_income],
    'Age': [age],
    'JobRole_Sales Representative': [int(job_role_sales_representative)],
    'YearsWithCurrManager': [years_with_curr_manager],
    'StockOptionLevel': [stock_option_level],
    'YearsAtCompany': [years_at_company],
    'JobInvolvement': [job_involvement],
    'BusinessTravel_Travel_Frequently': [int(business_travel_frequent)],
    'JobSatisfaction': [job_satisfaction],
    'EnvironmentSatisfaction': [environment_satisfaction]
}

# Predict button
if st.button('Predict Attrition'):
    prediction, probability = predict_attrition(user_data)
    if prediction == 0:
        st.success(f'Prediction: The employee is likely to stay. (Probability of leaving: {probability:.2f})')
    else:
        st.error(f'Prediction: The employee is likely to leave. (Probability of leaving: {probability:.2f})')


