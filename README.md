# 💳 Credit Risk Prediction System

## 📌 Overview

This project builds an end-to-end Machine Learning system to predict whether a customer is likely to default on a loan. It combines data preprocessing, feature engineering, model training, explainability, and deployment into a single pipeline.

The system uses **XGBoost** for high-performance prediction, **SMOTE** to handle class imbalance, and **SHAP (Explainable AI)** to interpret model decisions. A **Streamlit web application** is developed to provide real-time predictions and insights.

---

## 🎯 Problem Statement

Loan defaults lead to significant financial losses for banks and financial institutions. This project aims to predict the probability of customer default in advance, enabling better risk assessment and informed decision-making.

---

## 📂 Dataset

The dataset contains financial and behavioral attributes of customers such as:

* Income
* Debt ratio
* Credit history
* Payment behavior

These features are used to predict the likelihood of loan default.

---

## ⚙️ How It Works

1. User inputs customer details via Streamlit UI
2. Data is preprocessed using trained pipeline
3. XGBoost model predicts default probability
4. SHAP explains feature contribution
5. System outputs decision: **Approve / Reject / Review**

---

## 🚀 Live Demo

👉 https://migt5smydxp4borpwp9pt3.streamlit.app

---

## 🚀 Key Features

* End-to-end ML pipeline (EDA → Feature Engineering → Modeling → Deployment)
* Handles imbalanced data using **SMOTE**
* High-performance **XGBoost model**
* Real-time prediction using **Streamlit app**
* Risk-based decision system (Approve / Reject / Review)
* Explainability using **SHAP values**
* Feature engineering for improved accuracy

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

## 📊 Model Performance

* **ROC-AUC Score:** ~0.83
* **Accuracy:** ~86%
* Strong performance in identifying high-risk customers
* Focused on improving recall for minority (default) class

---

## 📸 Application Demo

### 🔹 App Interface

![App UI](app_ui.png)

User-friendly interface for entering customer details.

---

### 🔹 Prediction Result

![Prediction](prediction.png)

Displays:

* Default probability
* Risk level
* Final decision
* Key insights

---

### 🔹 SHAP Explainability

![SHAP](shap_plot.png)

Visual explanation of how each feature impacts predictions.

---

### 🔹 Feature Importance

![Feature Importance](feature_importance.png)

Shows top features influencing the model.

---

## 📊 Additional Analysis

### 🔹 Confusion Matrix

![Confusion Matrix](confusion_matrix.png)

Evaluates model classification performance.

---

### 🔹 Correlation Heatmap

![Heatmap](heatmap.png)

Shows relationships between features.

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

* Identifies high-risk customers early
* Helps reduce loan default losses
* Enables data-driven financial decisions

---

## 🔮 Future Improvements

* Hyperparameter tuning
* Cloud deployment (AWS / GCP / Azure)
* REST API integration

---

## 👨‍💻 Author

**Yeshwanth Reddy M**
🔗 GitHub: https://github.com/manneti-yeswanth
🔗 LinkedIn: www.linkedin.com/in/manneti-yeswanth-reddy-2758693b6
