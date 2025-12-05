import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

# Load saved model & feature columns
model = joblib.load("best_model 17.Heart Attack.joblib")
feature_columns = joblib.load("17.Heart Attack.joblib")

st.set_page_config(
    page_title="❤️ Heart Attack Prediction",
    layout="wide",
    page_icon="❤️"
)

# --- Header ---
st.title("❤️ Heart Attack Prediction Dashboard")
st.markdown("""
This application predicts the **risk of heart attack** based on patient health parameters.  
Enter the details on the left panel and click **Predict** to see the result.
""")

# --- Sidebar Input Section ---
st.sidebar.header("🧍‍♂️ Patient Information")

user_data = {}

for col in feature_columns:
    if "age" in col.lower():
        user_data[col] = st.sidebar.number_input(f"{col}", min_value=0, max_value=120, value=45)
    elif "sex" in col.lower():
        user_data[col] = st.sidebar.selectbox(f"{col}", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    elif "bp" in col.lower():
        user_data[col] = st.sidebar.number_input(f"{col}", min_value=50, max_value=250, value=120)
    elif "chol" in col.lower():
        user_data[col] = st.sidebar.number_input(f"{col}", min_value=50, max_value=600, value=200)
    elif "sugar" in col.lower():
        user_data[col] = st.sidebar.selectbox(f"{col}", [0, 1], format_func=lambda x: "Normal" if x == 0 else "High")
    else:
        user_data[col] = st.sidebar.number_input(f"{col}", value=0.0)

input_df = pd.DataFrame([user_data])

# --- Main Layout ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Entered Patient Data")
    st.dataframe(input_df)

with col2:
    st.subheader("⚙️ Model Details")
    st.write(f"**Model Type:** {type(model).__name__}")
    st.write(f"**Number of Features:** {len(feature_columns)}")

# --- Prediction ---
if st.button("🔍 Predict"):
    try:
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1] if hasattr(model, "predict_proba") else 0

        st.markdown("---")
        st.subheader("🎯 Prediction Result")

        colA, colB = st.columns(2)

        with colA:
            if prediction == 1:
                st.error("⚠️ **High Risk of Heart Attack!**")
            else:
                st.success("✅ **Low Risk of Heart Attack.**")

        with colB:
            # --- Gauge Meter (Plotly) ---
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=prob * 100,
                title={'text': "Risk Probability (%)"},
                gauge={'axis': {'range': [0, 100]},
                       'bar': {'color': "crimson" if prob > 0.5 else "green"},
                       'steps': [
                           {'range': [0, 50], 'color': "#9BF0A8"},
                           {'range': [50, 75], 'color': "#FFD966"},
                           {'range': [75, 100], 'color': "#F45B69"}
                       ]}
            ))
            st.plotly_chart(fig, use_container_width=True)

        # --- Feature Importance (if available) ---
        st.markdown("---")
        st.subheader("📊 Feature Importance")

        if hasattr(model, "feature_importances_"):
            importances = model.feature_importances_
            feat_imp = pd.DataFrame({"Feature": feature_columns, "Importance": importances})
            feat_imp = feat_imp.sort_values(by="Importance", ascending=False)

            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(x="Importance", y="Feature", data=feat_imp, palette="viridis", ax=ax)
            st.pyplot(fig)
        else:
            st.info("This model type does not provide feature importance.")

        st.markdown("---")
        st.caption("Developed by Manikandan 🧠 | Powered by Streamlit & Scikit-Learn")

    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")
