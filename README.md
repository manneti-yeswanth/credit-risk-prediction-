# 💳 Credit Risk Prediction System

## 📌 Overview

This project focuses on predicting whether a customer is likely to default on a loan using Machine Learning.

I built an end-to-end pipeline starting from data preprocessing to model deployment. The system uses an XGBoost model for prediction and handles imbalanced data using SMOTE. A Streamlit web app is created to allow users to input customer details and get real-time predictions.

To make the model more transparent, SHAP (Explainable AI) is used to understand how each feature contributes to the prediction. I also added a simple decision system (Approve / Reject / Review) based on the predicted risk.

---

## 🚀 Live Demo

👉 https://migt5smydxp4borpwp9pt3.streamlit.app

---

## 🚀 Key Features

* End-to-end ML pipeline (data preprocessing → modeling → deployment)
* Handling imbalanced data using SMOTE
* XGBoost model for prediction
* Interactive Streamlit web application
* Risk scoring with decision system (Approve / Reject / Review)
* Explainability using SHAP
* Feature engineering for better model performance

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* SHAP
* Matplotlib, Seaborn
* Streamlit

---

## 📸 Application Demo

### 🔹 App Interface

![App UI](app_ui.png)

User-friendly interface for entering customer details and predicting credit risk.

---

### 🔹 Prediction Result

![Prediction](prediction.png)

Displays predicted risk level, probability score, final decision, and key insights.

---

### 🔹 Feature Importance

![Feature Importance](feature_importance.png)

Shows which features contribute the most to the model predictions.

---

### 🔹 SHAP Explainability

![SHAP](shap_plot.png)

Explains how each feature affects an individual prediction using SHAP waterfall plot.

---

## 📊 Additional Analysis

### 🔹 Confusion Matrix

![Confusion Matrix](confusion_matrix.png)

Used to evaluate model performance on test data.

---

### 🔹 Correlation Heatmap

![Heatmap](heatmap.png)

Shows relationships between different financial features.

---

## 📁 Project Structure

* app.py
* credit_risk_prediction.ipynb
* loan_model.pkl
* columns.pkl
* requirements.txt

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📈 Business Impact

* Helps identify high-risk customers early
* Reduces loan default losses
* Supports data-driven decision making

---

## 🔮 Future Improvements

* Hyperparameter tuning
* Cloud deployment (AWS / GCP / Azure)
* REST API integration

---

## 👨‍💻 Author

**Yeshwanth Reddy M**
🔗 GitHub: https://github.com/manneti-yeswanth
🔗 LinkedIn: (Add your LinkedIn profile link)
