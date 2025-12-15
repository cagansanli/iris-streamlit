import streamlit as st
from predict import predict

st.title("Iris Flower Prediction App Pro Max 🌸")

sepal_length = st.number_input("Sepal Length", min_value=0.0, step=0.1)
sepal_width = st.number_input("Sepal Width", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length", min_value=0.0, step=0.1)
petal_width = st.number_input("Petal Width", min_value=0.0, step=0.1)

if st.button("Predict"):
    result = predict([sepal_length, sepal_width, petal_length, petal_width])
    st.success(f"Predicted species: {result}")
