# Business Value Calculation for Churn Prediction Model
# XGBoost Model Results Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# XGBoost Confusion Matrix Results
TN = 38967  # Correctly identified non-churners
FP = 5976   # False alarms - offered retention to non-churners
FN = 3789   # Missed churners - CRITICAL FAILURE
TP = 52310  # Caught churners - INTERVENTION OPPORTUNITY

# Total customers in test set
total_customers = TN + FP + FN + TP
churners = TP + FN
non_churners = TN + FP

print("="*80)
print("BUSINESS VALUE ANALYSIS: XGBoost Churn Prediction Model")
print("="*80)
print(f"\nTest Set Statistics:")
print(f"Total Customers: {total_customers:,}")
print(f"Actual Churners: {churners:,} ({churners/total_customers:.1%})")
print(f"Actual Non-Churners: {non_churners:,} ({non_churners/total_customers:.1%})")
print(f"\nModel Performance:")
print(f"True Positives (Caught Churners): {TP:,}")
print(f"False Negatives (Missed Churners): {FN:,}")
print(f"False Positives (Unnecessary Offers): {FP:,}")
print(f"True Negatives (Correctly Identified): {TN:,}")

# ============================================================================
# FINANCIAL ASSUMPTIONS
# ============================================================================

# Customer Lifetime Value - Average revenue per customer over their lifetime
LTV = 1200  # dollars

# Cost to execute retention intervention (personalized offers, discounts, account manager time)
intervention_cost = 75  # dollars per customer

# Success rate of retention interventions (industry average 30-45%)
intervention_success_rate = 0.40  # 40% of at-risk customers are saved

# Baseline churn cost (no model scenario)
baseline_churn_rate = churners / total_customers  # 55.52%

print(f"\n" + "="*80)
print("FINANCIAL ASSUMPTIONS")
print("="*80)
print(f"Customer Lifetime Value (LTV): ${LTV:,}")
print(f"Intervention Cost per Customer: ${intervention_cost:,}")
print(f"Intervention Success Rate: {intervention_success_rate:.0%}")
print(f"Baseline Churn Rate (No Model): {baseline_churn_rate:.2%}")

# ============================================================================
# SCENARIO 1: WITHOUT PREDICTIVE MODEL (Baseline)
# ============================================================================

# Without model: No targeted interventions, all churners are lost
baseline_lost_revenue = churners * LTV
baseline_total_cost = baseline_lost_revenue

print(f"\n" + "="*80)
print("SCENARIO 1: WITHOUT PREDICTIVE MODEL (Baseline)")
print("="*80)
print(f"Strategy: No churn prediction, no retention interventions")
print(f"\nFinancial Impact:")
print(f"  Lost Revenue (All Churners): ${baseline_lost_revenue:,.0f}")
print(f"  Intervention Costs: $0 (no interventions)")
print(f"  TOTAL COST TO BUSINESS: ${baseline_total_cost:,.0f}")

# ============================================================================
# SCENARIO 2: WITH XGBOOST PREDICTIVE MODEL
# ============================================================================

# Revenue saved by catching churners (TP)
saved_revenue_from_TP = TP * LTV * intervention_success_rate

# Revenue lost from missed churners (FN)
lost_revenue_from_FN = FN * LTV

# Intervention costs (for both TP and FP - we intervene on both)
total_intervention_cost = (TP + FP) * intervention_cost

# Net financial impact
model_total_cost = lost_revenue_from_FN + total_intervention_cost - saved_revenue_from_TP

print(f"\n" + "="*80)
print("SCENARIO 2: WITH XGBOOST PREDICTIVE MODEL")
print("="*80)
print(f"Strategy: Predictive model identifies at-risk customers for targeted retention")
print(f"\nRevenue Outcomes:")
print(f"  Revenue Saved (TP × LTV × Success Rate): ${saved_revenue_from_TP:,.0f}")
print(f"    └─ {TP:,} churners identified × ${LTV} × {intervention_success_rate:.0%} = ${saved_revenue_from_TP:,.0f}")
print(f"\n  Revenue Lost (FN × LTV): ${lost_revenue_from_FN:,.0f}")
print(f"    └─ {FN:,} churners missed × ${LTV} = ${lost_revenue_from_FN:,.0f}")
print(f"\nCosts:")
print(f"  Intervention Costs ((TP+FP) × Cost): ${total_intervention_cost:,.0f}")
print(f"    └─ {TP+FP:,} customers targeted × ${intervention_cost} = ${total_intervention_cost:,.0f}")
print(f"\nNET FINANCIAL IMPACT:")
print(f"  Total Cost to Business: ${model_total_cost:,.0f}")
print(f"    (Lost Revenue + Intervention Costs - Saved Revenue)")

# ============================================================================
# ROI CALCULATION
# ============================================================================

net_savings = baseline_total_cost - model_total_cost
roi_percentage = (net_savings / baseline_total_cost) * 100

print(f"\n" + "="*80)
print("RETURN ON INVESTMENT (ROI)")
print("="*80)
print(f"Baseline Cost (No Model): ${baseline_total_cost:,.0f}")
print(f"Model Cost (With Prediction): ${model_total_cost:,.0f}")
print(f"\n💰 NET SAVINGS: ${net_savings:,.0f}")
print(f"📈 ROI: {roi_percentage:.2f}%")
print(f"\n🎯 Cost Reduction: {(1 - model_total_cost/baseline_total_cost):.1%}")

# Per customer savings
savings_per_customer = net_savings / total_customers
print(f"💵 Savings Per Customer: ${savings_per_customer:.2f}")

# ============================================================================
# DETAILED BREAKDOWN TABLE
# ============================================================================

breakdown_data = {
    'Metric': [
        'Total Customers',
        'Model Accuracy',
        'Model Recall (Churn)',
        '',
        'True Positives (Caught)',
        'False Negatives (Missed)',
        'False Positives (False Alarms)',
        '',
        'Customers Saved (TP × Success Rate)',
        'Revenue Saved',
        'Revenue Lost',
        'Intervention Costs',
        '',
        'Net Savings vs Baseline',
        'ROI %',
        'Savings Per Customer'
    ],
    'Value': [
        f"{total_customers:,}",
        "90%",
        "93%",
        "",
        f"{TP:,}",
        f"{FN:,}",
        f"{FP:,}",
        "",
        f"{int(TP * intervention_success_rate):,}",
        f"${saved_revenue_from_TP:,.0f}",
        f"${lost_revenue_from_FN:,.0f}",
        f"${total_intervention_cost:,.0f}",
        "",
        f"${net_savings:,.0f}",
        f"{roi_percentage:.2f}%",
        f"${savings_per_customer:.2f}"
    ]
}

breakdown_df = pd.DataFrame(breakdown_data)

print(f"\n" + "="*80)
print("COMPREHENSIVE BUSINESS IMPACT SUMMARY")
print("="*80)
print(breakdown_df.to_string(index=False))

# ============================================================================
# SENSITIVITY ANALYSIS
# ============================================================================

print(f"\n" + "="*80)
print("SENSITIVITY ANALYSIS")
print("="*80)

# Test different intervention success rates
success_rates = [0.25, 0.30, 0.35, 0.40, 0.45, 0.50]
sensitivity_results = []

for rate in success_rates:
    saved = TP * LTV * rate
    lost = FN * LTV
    costs = (TP + FP) * intervention_cost
    model_cost = lost + costs - saved
    savings = baseline_total_cost - model_cost
    roi = (savings / baseline_total_cost) * 100

    sensitivity_results.append({
        'Success_Rate': f"{rate:.0%}",
        'Revenue_Saved': f"${saved:,.0f}",
        'Net_Savings': f"${savings:,.0f}",
        'ROI': f"{roi:.2f}%"
    })

sensitivity_df = pd.DataFrame(sensitivity_results)
print("\nNet Savings at Different Intervention Success Rates:")
print(sensitivity_df.to_string(index=False))

# ============================================================================
# ANNUALIZED PROJECTIONS
# ============================================================================

# Assuming quarterly or annual projections
# Test set represents 20% of total data
total_customer_base = total_customers * 5  # Approximate full customer base

annual_net_savings = net_savings * 5
annual_customers_saved = int(TP * intervention_success_rate * 5)

print(f"\n" + "="*80)
print("ANNUALIZED BUSINESS IMPACT PROJECTIONS")
print("="*80)
print(f"Estimated Total Customer Base: {total_customer_base:,}")
print(f"\n💰 Projected Annual Savings: ${annual_net_savings:,.0f}")
print(f"👥 Projected Customers Retained Annually: {annual_customers_saved:,}")
print(f"📊 Projected Annual ROI: {roi_percentage:.2f}%")

# ============================================================================
# VISUALIZATION OUTPUTS
# ============================================================================

print(f"\n" + "="*80)
print("Generating visualizations...")
print("="*80)

# This script generates the calculations
# Visualizations will be created in the Jupyter notebook
