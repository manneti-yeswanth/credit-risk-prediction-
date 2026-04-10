# 💳 Credit Risk Prediction System

## 📌 Overview

An end-to-end Machine Learning project that predicts the probability of a customer defaulting on a loan.

The system uses XGBoost for prediction, handles imbalanced data using SMOTE, and provides an interactive Streamlit web application for real-time predictions. It also integrates SHAP to explain model decisions and includes a simple decision system (Approve / Reject / Review).

---

## 🚀 Live Demo

👉 https://migt5smydxp4borpwp9pt3.streamlit.app

---

## 🚀 Key Features

* End-to-end ML pipeline (data preprocessing → modeling → deployment)
* Imbalanced data handling using SMOTE
* XGBoost model
* Streamlit web application
* Model evaluation using multiple metrics
* SHAP explainability
* Decision system (Approve / Reject / Manual Review)

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

User-friendly interface for entering customer details and predicting credit risk

---

### 🔹 Prediction Result

![Prediction](prediction.png)

Displays predicted risk level along with probability and decision

---

### 🔹 Confusion Matrix

![Confusion Matrix](confusion_matrix.png)

Shows model performance on test data

---

### 🔹 Feature Importance

![Feature Importance](feature_importance.png)

Identifies the most important features influencing predictions

---

### 🔹 Correlation Heatmap

![Heatmap](heatmap.png)

Shows relationships between financial features

---

### 🔹 SHAP Explainability

![SHAP](shap_plot.png)

Explains how each feature contributes to individual predictions

---

## 📁 Project Structure

* app.py
* credit_risk_prediction.ipynb
* loan_model.pkl
* columns.pkl
* requirements.txt

---

## ▶️ Run Locally

pip install -r requirements.txt
streamlit run app.py

---

## 📈 Business Impact

* Helps identify high-risk customers early
* Reduces loan default losses
* Supports data-driven decision making

---

## 🔮 Future Improvements

* Hyperparameter tuning
* Cloud deployment
* API integration

---

## 👨‍💻 Author

Yeshwanth Reddy M
GitHub: https://github.com/manneti-yeswanth
LinkedIn: (Add your link)
