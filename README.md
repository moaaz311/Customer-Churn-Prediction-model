# Customer Churn Prediction App

## 📌 Project Overview

This project is a simple **Customer Churn Prediction** web application built using **Streamlit** and a trained machine learning model.
The app allows users to enter customer information and predict whether the customer is likely to churn or stay.

---

## ⚠️ Challenge Faced

During model development, the initial approach used **Gaussian Naive Bayes**. However, after evaluation, the model showed weak performance in detecting churn customers, especially in terms of recall and ROC-AUC.

The main challenges were:

* Small dataset size (100 records)
* Class imbalance between churn and non-churn customers
* Limited number of input features
* GaussianNB assumptions not fitting the data well

To address this challenge and improve the model’s ability to detect customers at risk of leaving, the model was replaced with **Logistic Regression** using `class_weight='balanced'`.

This change resulted in:

* Better recall for churn customers
* More meaningful business predictions
* Improved overall model reliability

---

## 🚀 Features

* Preview the churn dataset
* Input customer details (Age, Tenure, Sex)
* Predict customer churn using a trained Logistic Regression model
* Display churn and stay probabilities
* Interactive Streamlit interface

---

## 🧰 Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Joblib
* Scikit-learn

---

## 📂 Project Structure

├── Customer_Churn_PredictionAPP.py
├── churn_dataset.xlsx
├── model_Logistic.pkl
└── README.md

---


## ▶️ How to Run the App

```id="1ztm5g"
python -m streamlit run Customer_Churn_PredictionAPP.py
```

Then open your browser at:

```id="vbdcrr"
http://localhost:8501
```

---

## 🧠 How It Works

1. The dataset is loaded and displayed.
2. The trained Logistic Regression model is loaded using Joblib.
3. User inputs customer information.
4. The model predicts:

   * Stay probability
   * Churn probability
5. The result is displayed in the Streamlit interface.

---

## 📊 Input Features

* **Age** — Customer age
* **Tenure** — Number of months with the company
* **Sex** — Male or Female

---

## 📈 Model Performance Notes

* Logistic Regression improved **recall for churn customers** compared to the initial approach.
* ROC-AUC indicates performance slightly above random baseline.
* Performance is constrained by the **small dataset size** and **limited feature set**.

---

## 🔮 Future Improvements

* Add more customer behavioral features
* Increase dataset size
* Perform hyperparameter tuning
* Deploy the app online (Streamlit Cloud)
* Add advanced visualizations


⭐ *This project is part of the ITI Data Mining training tasks.*
