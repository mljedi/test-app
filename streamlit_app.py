import streamlit as st
import pickle
# Load the pre-trained model

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set up the Streamlit app
st.title("Social Ads Purchase Prediction")

# Create input fields for age and salary
age = st.number_input("Age", min_value=0, max_value=100, value=30)
salary = st.number_input("Salary", min_value=0, step=1000, value=50000)

# Make prediction when the user clicks the 'Predict' button
if st.button("Predict"):
    # Prepare input data for prediction
    input_data = [[age, salary]]

    # Perform prediction
    prediction = model.predict(input_data)

    # Display the prediction
    if prediction[0] == 1:
        st.success("User is likely to make a purchase.")
    else:
        st.error("User is unlikely to make a purchase.")
