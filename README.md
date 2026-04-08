# 💳 Credit Risk Prediction System

## 📌 Overview

An end-to-end machine learning project that predicts the probability of a customer defaulting on a loan.

The system uses **XGBoost** for prediction, handles imbalanced data using **SMOTE**, and provides an interactive **Streamlit web application** for real-time predictions. The project also includes **Explainable AI (SHAP)** to interpret model decisions.

---

## 🚀 Key Features

* End-to-end ML pipeline
* Imbalanced data handling using SMOTE
* High-performance XGBoost model
* Interactive Streamlit UI
* Model evaluation with multiple metrics
* Explainability using SHAP

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Imbalanced-learn (SMOTE)
* SHAP
* Streamlit
* Matplotlib, Seaborn

---

## 📸 Application Demo

### 🔹 App Interface

![App UI](app_ui.png)

### 🔹 Prediction Result

![Prediction](prediction.png)

---

## 📊 Model Evaluation

### 🔹 Confusion Matrix

![Confusion Matrix](confusion_matrix.png)

### 🔹 Feature Importance

![Feature Importance](feature_importance.png)

### 🔹 Correlation Heatmap

![Heatmap](heatmap.png)

---

## 🔍 Explainability (SHAP)

SHAP (SHapley Additive exPlanations) is used to understand how each feature contributes to the prediction.

![SHAP](shap_plot.png)

---

## 📁 Project Structure

```
app.py
credit_risk_prediction.ipynb
loan_model.pkl
columns.pkl
requirements.txt
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Future Improvements

* Model tuning for better performance
* Deploy using cloud platforms
* Add API support

---

## 👨‍💻 Author

Yeshwanth
