# Customer Churn Prediction with Business ROI Analysis

![Business Case Overview](business_case.png)

An end-to-end machine learning project that predicts customer churn and translates model performance into clear business value.

This project is designed to answer two questions recruiters and business stakeholders care about:
1. Can the model accurately identify at-risk customers?
2. Does acting on the model create measurable financial impact?

---

## Executive Summary

- Built a churn prediction pipeline using **XGBoost** on a large customer dataset (100k+ records in test set).
- Achieved strong churn detection performance with approximately:
	- **Accuracy:** ~90%
	- **Churn Recall:** ~93%
- Converted model output into business outcomes using a cost-benefit framework:
	- Estimated **net savings:** **$20.7M** (test-scope scenario under stated assumptions)
	- Estimated **cost reduction / ROI impact:** **30.80%**
	- Estimated annualized savings projection: **$103.7M**

This is not just a classification notebook. It is a business-oriented analytics solution that connects data science outputs to decision-making.

---

## Business Problem

Customer churn directly impacts recurring revenue and growth. Retaining high-risk customers is often cheaper than acquiring new ones, but retention campaigns are expensive if poorly targeted.

Goal:
- Predict which customers are likely to churn.
- Prioritize retention actions on the right segment.
- Quantify whether intervention strategy is financially justified.

---

## Project Highlights

- Full lifecycle workflow: data loading, cleaning, feature preparation, modeling, evaluation, and business translation.
- Dedicated **business value analysis** script to estimate financial upside from model-guided retention.
- Clear confusion-matrix-driven operational interpretation:
	- **TP:** churners correctly identified
	- **FN:** churners missed (critical revenue loss)
	- **FP:** unnecessary retention offers
	- **TN:** correct non-churn identification

---

## Tech Stack

- **Languages:** Python
- **Core Libraries:** pandas, numpy
- **Modeling:** XGBoost
- **Visualization:** matplotlib, seaborn
- **Environment:** Jupyter Notebook

---

## Key Data Science Skills Demonstrated

- Problem framing for real-world business context
- Data preprocessing and feature handling
- Classification model training and evaluation
- Metric interpretation beyond accuracy (recall, confusion matrix impacts)
- Model-to-business translation (ROI and sensitivity analysis)
- Scenario analysis and annualized value projection

---

## Business Impact Framework (from `business_value_analysis.py`)

### Model Confusion Matrix Inputs

- **TP:** 52,310
- **FN:** 3,789
- **FP:** 5,976
- **TN:** 38,967

### Financial Assumptions

- Customer Lifetime Value (LTV): **$1,200**
- Retention intervention cost: **$75/customer**
- Intervention success rate: **40%**

### Estimated Outcomes

- Baseline churn cost (no model): **$67,318,800**
- Model-informed strategy cost: **$46,581,450**
- **Net savings:** **$20,737,350**
- **ROI / Cost reduction impact:** **30.80%**
- **Fewer customers lost:** **37.3% reduction**

### Sensitivity + Scaling

- Includes sensitivity analysis across intervention success rates (25%-50%).
- Includes scaled annual projections for broader customer base impact.

> Note: Financial outputs are scenario-based and depend on assumptions. They are intended to support strategic decision-making, not to replace production finance models.

---

## Repository Structure

```text
.
|-- business_value_analysis.py
|-- churn_prediction.ipynb
|-- churn_prediction_copy.ipynb
|-- churn_prediction_final.ipynb
|-- data/
|   |-- customer_churn_dataset-training-master.csv
|   `-- customer_churn_dataset-testing-master.csv
`-- README.md
```

---

## How to Run

1. Clone this repository.
2. Create and activate a Python environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Open and run the final notebook:

```bash
jupyter notebook churn_prediction_final.ipynb
```

5. Run business value analysis:

```bash
python business_value_analysis.py
```

6. Launch the Streamlit dashboard:

```bash
streamlit run streamlit_app.py
```

---

## Streamlit Deployment

The dashboard is ready to deploy on Streamlit Community Cloud.

1. Push this repository to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Create a new app and point it to `streamlit_app.py`.
4. Make sure `requirements.txt` is included at the repository root so Streamlit can install the packages.
5. Deploy.

If you want a real scoring dashboard later, save the trained preprocessing and model pipeline from the notebook as a file such as `model.joblib`, then load it inside `streamlit_app.py`.

---

## Recruiter Snapshot

If you are hiring for Data Scientist / ML Analyst / Decision Scientist roles, this project demonstrates:

- Ability to build a practical churn model
- Strong understanding of evaluation trade-offs (especially recall for churn)
- Business communication skill: turning technical metrics into dollar impact
- End-to-end ownership mindset from exploration to executive-level insights

---

## License

This project is open-sourced under the terms in the `LICENSE` file.

