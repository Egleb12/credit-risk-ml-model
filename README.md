# 📈 Credit Risk Prediction Model  
### (Financial Statements + Machine Learning)

This project builds a machine learning model that predicts corporate default risk using real financial statement data.  
It uses balance sheet, income statement, and cashflow ratios to classify companies as safe or risky and generates a 0–100 credit risk score.

Project Overview

This model analyzes fundamental financial health by calculating a set of core financial ratios:

Leverage Ratio

Debt-to-Assets

Current Ratio

Profit Margin

Return on Assets (ROA)

Operating Margin

Interest Coverage

Cashflow Strength Metrics

It then trains a machine learning model to predict credit risk and assigns each company a risk score using a scaled logistic regression probability.

Machine Learning Pipeline

✔ Data Collection
– Pulled 10 real public companies using the Yahoo Finance API.
– Extracted balance sheet, income statement, and cashflow data.

✔ Feature Engineering
– Calculated 8 financial ratios.
– Cleaned missing data + normalized inputs.

✔ Modeling
– Logistic Regression classifier
– Target variable: manually-defined default risk (safe = 0, high-risk = 1)

✔ Outputs
– Predicted risk class (safe / distressed)
– Risk probability converted to a 0–100 risk score

Example Output
Company	Actual Default Risk	Predicted Score
AAPL	0	70.3
MSFT	0	92.0
COST	0	77.7
JPM	0	83.0
JNJ	0	61.7
XOM	0	48.3
RADQ	1	9.3
SAVE	1	9.3
PTON	1	16.3
CVNA	1	24.3
BBBYQ	1	9.3


🧾 Files in This Repository
File	Description
credit-risk-model.ipynb	Full end-to-end notebook with data collection, cleaning, ratios, and ML model
01-data-collection.ipynb	Script that pulls financial data using the Yahoo Finance API
credit_risk_results.csv	Final dataset containing ratios + predicted credit risk scores
README.md	Project documentation


🛠️ Technologies Used

Python

Pandas

NumPy

scikit-learn

yfinance API

Jupyter Notebook

Logistic Regression (ML)

🎯 Why This Project Matters

Credit risk modeling is widely used in:

Investment banking

Private credit

Hedge funds

Credit rating analysis

Corporate finance

Risk management

This project demonstrates:

✔ Financial statement analysis
✔ Data engineering
✔ Feature creation from accounting data
✔ Real machine learning implementation
✔ Predictive scoring
✔ Model interpretation

Perfect for showcasing quantitative finance + programming skills to recruiters.


🧩 Future Improvements

Planned enhancements:

Add 50+ companies for deeper data

Pull 10-year financial history and analyze trends

Add advanced models (Random Forest, XGBoost)

Compare performance across ML algorithms

Build a Streamlit dashboard for interactive credit risk scoring


✨ Author

Evan Glebov
Finance + AIM FinTech @ Marquette
Python • Machine Learning • Corporate Finance • Data Analytics
