import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import shap

# ---------------- LOAD ----------------
model = joblib.load("loan_model.pkl")
columns = joblib.load("columns.pkl")

st.set_page_config(page_title="Credit Risk AI", layout="wide")

# ---------------- HEADER ----------------
st.markdown("""
<h1 style='text-align:center;color:#2c3e50;'>💳 Credit Risk Prediction System</h1>
<p style='text-align:center;color:gray;'>Explainable AI + Feature Engineering</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- INPUT ----------------
st.subheader("🧾 Enter Customer Details")

c1, c2, c3 = st.columns(3)

with c1:
    age = st.number_input("Age", 18, 100, 30)
    income = st.number_input("Monthly Income", 0, 50000, 5000)
    dependents = st.number_input("Dependents", 0, 10, 1)

with c2:
    revolving = st.slider("Revolving Utilization", 0.0, 2.0, 0.5)
    debt_ratio = st.slider("Debt Ratio", 0.0, 2.0, 0.5)
    open_credit = st.number_input("Open Credit Lines", 0, 20, 5)

with c3:
    late_30 = st.slider("30-59 Days Late", 0, 10, 0)
    late_60 = st.slider("60-89 Days Late", 0, 10, 0)
    late_90 = st.slider("90 Days Late", 0, 10, 0)
    real_estate = st.number_input("Real Estate Loans", 0, 10, 1)

predict = st.button("🚀 Predict Loan Risk")

# ---------------- PREDICT ----------------
if predict:

    # -------- FEATURE ENGINEERING --------
    income_per_person = income / (dependents + 1)
    debt_per_income = debt_ratio / (income + 1)
    total_late = late_30 + late_60 + late_90

    input_data = pd.DataFrame([[
        revolving, age, late_30, debt_ratio, income,
        open_credit, late_90, real_estate, late_60, dependents,
        income_per_person, debt_per_income, total_late
    ]], columns=columns)

    prob = model.predict_proba(input_data)[0][1]

    st.markdown("---")
    st.subheader("📊 Prediction Result")

    # -------- COLOR CARDS --------
    if prob < 0.35:
        st.success(f"✅ Low Risk ({prob*100:.2f}%)")

    elif prob < 0.65:
        st.warning(f"🟡 Medium Risk ({prob*100:.2f}%)")

    else:
        st.error(f"🔴 High Risk ({prob*100:.2f}%)")

    # -------- WARNINGS --------
    if total_late > 3:
        st.error("🚨 Too many late payments")

    if debt_ratio > 1:
        st.warning("⚠️ High Debt Ratio")

    if income < 3000:
        st.warning("⚠️ Low Income")

    # -------- FEATURE IMPACT --------
    with st.expander("🔍 Feature Impact"):
        st.json({
            "Total Late Payments": total_late,
            "Debt Ratio": debt_ratio,
            "Income per Person": income_per_person,
            "Debt per Income": debt_per_income
        })

    # -------- FEATURE IMPORTANCE --------
    with st.expander("📈 Feature Importance"):
        importances = model.feature_importances_
        feat_imp = pd.Series(importances, index=columns).sort_values(ascending=False)

        fig, ax = plt.subplots()
        feat_imp.head(10).plot(kind='barh', ax=ax)
        ax.invert_yaxis()
        st.pyplot(fig)

    # -------- SHAP --------
    with st.expander("🧠 Explainable AI (SHAP)", expanded=True):

        explainer = shap.Explainer(model)
        shap_values = explainer(input_data)

        st.markdown("### 🔹 Waterfall (Individual Prediction)")
        fig1 = plt.figure()
        shap.plots.waterfall(shap_values[0], show=False)
        st.pyplot(fig1)

        st.markdown("### 🔹 Summary Plot")
        fig2 = plt.figure()
        shap.summary_plot(shap_values, input_data, show=False)
        st.pyplot(fig2)
