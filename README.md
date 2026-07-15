# Placement Analytics and Prediction System

An end-to-end placement intelligence project that goes beyond classification and turns student data into an analytics product for placement officers, departments, and recruiters.

## What this project does

- Builds an ETL pipeline from raw student data to cleaned analytics marts
- Loads SQL-ready staging tables and executive summary views
- Delivers an interactive Streamlit dashboard for placement analytics
- Trains machine learning models for placement prediction and salary estimation
- Adds placement risk scoring, explainable drivers, and improvement recommendations
- Produces branch, company, gender, and year-wise reporting views

## Business Problem

Colleges usually store placement records as flat CSV files, but the real value comes from answering questions like:

- Which branches are at risk?
- Which companies hire most often?
- What factors influence placement outcomes?
- Which students need intervention early?
- How have placement trends changed over time?

This project turns raw student records into a decision-support system for those questions.

## Architecture

```text
Raw Student CSV
    |
    v
Python ETL
    |
    v
Cleaned Dataset + Analytics Marts
    |
    v
SQL Staging + Views
    |
    v
Power BI / Executive Reporting
    |
    v
ML Prediction
    |
    v
Risk Score + Recommendations
    |
    v
Streamlit Dashboard
```

## Key Features

### ETL and Data Engineering

- Raw dataset ingestion
- Synthetic enrichment for communication skill, project count, company assignment, and cohort year
- Feature engineering for employability score, risk score, and intervention priority
- Cleaned CSV export for analytics and model training
- SQL-ready flat table for MySQL import

### Executive Analytics

- Overall placement rate
- Average package and highest package
- Internship conversion rate
- Eligible students and at-risk students
- Branch-wise placement performance
- Company hiring summary
- Gender distribution
- Year-wise placement trend

### ML Prediction

- Placement classification
- Salary prediction for placed students
- Model metadata export

### Decision Support

- Placement risk score
- Risk band: Low / Medium / High
- Explainability-style factor breakdown
- Personalized improvement recommendations

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Matplotlib
- Seaborn
- SQL / MySQL
- Power BI

## Folder Structure

```text
Placement-Analytics/
|-- data/
|   |-- raw/
|   |-- cleaned/
|   |-- marts/
|-- sql_analysis/
|-- notebooks/
|-- models/
|-- dashboard/
|-- images/
|-- reports/
|-- app.py
|-- prepare_project.py
|-- README.md
|-- requirements.txt
```

## Main Outputs

- `data/cleaned/placement_data_cleaned.csv`
- `data/marts/branch_kpi_summary.csv`
- `data/marts/company_kpi_summary.csv`
- `data/marts/yearly_placement_trend.csv`
- `data/marts/gender_placement_summary.csv`
- `data/marts/risk_band_summary.csv`
- `data/marts/at_risk_students.csv`
- `data/marts/executive_kpis.json`
- `models/placement_model.pkl`
- `models/salary_model.pkl`
- `models/model_metadata.json`

## SQL Analysis

The `sql_analysis/` folder contains:

- Schema definition
- Data import script
- Cleaning checks
- Reusable views
- Executive queries for:
  - Top recruiters
  - Branch package comparison
  - Gender placement rate
  - Internship vs non-internship outcomes
  - Students requiring intervention

## Streamlit App

Run the dashboard locally with:

```bash
streamlit run app.py
```

The app includes:

- Student prediction form
- Salary forecast
- Placement risk score
- Improvement suggestions
- Executive analytics dashboard
- Branch, company, and trend views

## How to Use

1. Place the raw CSV in the project root.
2. Run `python prepare_project.py` to build the cleaned dataset, marts, and models.
3. Start the dashboard with `streamlit run app.py`.
4. Use the SQL scripts and Power BI folder for reporting layers.

## Future Scope

- Native SHAP-based explainability
- Department-level dashboards by branch and batch
- Forecasting for future placement trends
- Live database integration instead of CSV-based ETL
- Power BI deployment and scheduled refreshes

## Note

Some columns in the enriched dataset are engineered for analytics and demo purposes, because the source CSV does not include every operational field needed for a full placement office workflow.

