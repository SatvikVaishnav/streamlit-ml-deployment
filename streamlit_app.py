import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

model = joblib.load("model.pkl")

st.title("Iris Flower Predictor")
st.write("Adjust the sliders to predict the Iris flower species.")

# Input features
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width", 0.1, 2.5, 0.2)

input_data = pd.DataFrame({
    'feature1': [sepal_length],
    'feature2': [sepal_width],
    'feature3': [petal_length],
    'feature4': [petal_width]
})

st.subheader("Input Data")
st.write(input_data)

prediction = model.predict(input_data)
proba = model.predict_proba(input_data)

st.subheader("Prediction")
st.write(f"Predicted Class: {prediction[0]}")

st.subheader("Probabilities")
st.write(proba)

fig, ax = plt.subplots()
sns.barplot(x=model.classes_, y=proba[0], ax=ax)
st.pyplot(fig)
