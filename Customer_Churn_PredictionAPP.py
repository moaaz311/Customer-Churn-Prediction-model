import pandas as pn
import numpy as np
import joblib
import streamlit as st

st.title("Customer Churn Prediction")

churn_df=pn.read_excel("churn_dataset.xlsx")
st.subheader("data set preview")
st.write(churn_df)

model=joblib.load("model_Gaussian,pkl")


age = st.number_input("Age", min_value=min(churn_df["Age"]), max_value=max(churn_df["Age"]), value=30)
tenure = st.number_input("Tenure (months)", min_value=min(churn_df["Tenure"]), max_value=max(churn_df["Tenure"]), value=12)
sex = st.selectbox("Sex", ["Male", "Female"])

sex_num = 1 if sex == "Male" else 0

st.subheader("prediction")
if st.button("Predict"):

    user_data = np.array([[age, tenure, sex_num]])

    prediction = model.predict(user_data)[0]

    proba = model.predict_proba(user_data)[0]
    st.write(f"Stay probability: {proba[0]*100:.0f}% 😊")
    st.write(f"Churn probability: {proba[1]*100:.0f}% ☹️")
   
    if prediction == 1:
        st.error("Customer will churn ❌")
    else:
        st.success("Customer will stay ✅")
        