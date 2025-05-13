import streamlit as st
import pandas as pd

st.title("Simple BMI Calculator")

height = st.number_input("Enter your height (in cm):")
weight = st.number_input("Enter your weight (in kg):")

if st.button("Calculate BMI"):
    bmi = weight / ((height / 100) ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")