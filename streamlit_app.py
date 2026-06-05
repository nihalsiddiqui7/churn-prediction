import streamlit as st
import requests

# --------------------------
# Page Config
# --------------------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# --------------------------
# Header
# --------------------------

st.title("📊 Customer Churn Prediction System")

st.markdown("""
Predict whether a customer is likely to churn based on
their subscription details and interaction history.
""")

st.divider()

# --------------------------
# Input Section
# --------------------------

col1, col2 = st.columns(2)

with col1:

    support_calls = st.number_input(
        "📞 Support Calls",
        min_value=0,
        value=5
    )

    payment_delay = st.number_input(
        "💳 Payment Delay (Days)",
        min_value=0,
        value=5
    )

    subscription_type = st.selectbox(
        "⭐ Subscription Type",
        ["Basic", "Standard", "Premium"]
    )

with col2:

    total_spend = st.number_input(
        "💰 Total Spend",
        min_value=0.0,
        value=1000.0
    )

    last_interaction = st.number_input(
        "🕒 Last Interaction (Days)",
        min_value=0,
        value=10
    )

    contract_length = st.selectbox(
        "📃 Contract Length",
        ["Monthly", "Quarterly", "Annual"]
    )

st.divider()

# --------------------------
# Prediction Button
# --------------------------

if st.button("🚀 Predict Churn", use_container_width=True):

    payload = {
        "support_calls": support_calls,
        "total_spend": total_spend,
        "payment_delay": payment_delay,
        "last_interaction": last_interaction,
        "subscription_type": subscription_type,
        "contract_length": contract_length
    }

    try:

        response = requests.post(
            "http://13.236.201.73:8000/predict",
            json=payload
        )

        if response.status_code == 200:

            result = response.json()

            prediction = result["prediction"]
            probability = result["churn_probability"]

            st.divider()

            st.subheader("Prediction Results")

            metric_col1, metric_col2 = st.columns(2)

            with metric_col1:
                st.metric(
                    "Churn Probability",
                    f"{probability:.2%}"
                )

            with metric_col2:
                st.metric(
                    "Prediction",
                    "Churn" if prediction == 1 else "No Churn"
                )

            # Risk Level

            if probability >= 0.80:

                st.error(
                    "🔴 Very High Risk Customer"
                )

            elif probability >= 0.50:

                st.warning(
                    "🟠 Moderate Risk Customer"
                )

            else:

                st.success(
                    "🟢 Low Risk Customer"
                )

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

    except Exception as e:

        st.error(
            f"Unable to connect to FastAPI server.\n\n{e}"
        )

# --------------------------
# Footer
# --------------------------

st.divider()

st.caption(
    "Built with XGBoost • FastAPI • Streamlit • Docker • MLflow • GitHub Actions"
)