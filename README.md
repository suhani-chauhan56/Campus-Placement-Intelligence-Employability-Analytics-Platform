<div align="center">

# 🎓 Placement Prediction & College Analytics

### Turning student academic and skill data into placement predictions, SQL insights, and dashboard-ready analytics

**Python** -> **MySQL** -> **Power BI** -> **Machine Learning**

![Python](https://img.shields.io/badge/Python-Pandas%20%7C%20Sklearn-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Partially%20Complete-yellow?style=for-the-badge)

### 🚀 [Live Demo - Try the Prediction App](https://placement-prediction-college-analytics-j7evnb2vmmmjxmnc6g4fdq.streamlit.app/)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://placement-prediction-college-analytics-j7evnb2vmmmjxmnc6g4fdq.streamlit.app/)

</div>

---

Every placement season, colleges sit on a goldmine of data: CGPA, internships, certifications, coding scores, communication scores, and placement outcomes. This project turns that data into a complete analytics product instead of just a prediction script.

It combines:

- data cleaning and feature engineering
- SQL schema and analysis
- Power BI reporting
- machine learning for placement and salary prediction

---

## Executive Summary

Analyzed **12,000 student records** across 6 branches and 13 recruiting companies to understand what drives campus placements and expected package outcomes. Built classification and regression models to predict **Placement Status** and **Expected Package (LPA)**.

---

## Business Problem

The placement cell and department teams need faster answers to questions like:

- Which branches are performing best?
- Which companies are hiring the most?
- Which students need early intervention?
- How do internships and skills affect placement outcomes?
- What is the expected salary for a given student profile?

This project helps answer those questions in a structured way.

---

## Architecture

```text
Raw Student Dataset
    |
    v
Python ETL
    |
    v
Cleaned Dataset
    |
    v
SQL Analysis Layer
    |
    v
EDA and Power BI Dashboard
    |
    v
Machine Learning Models
    |
    v
Placement Prediction + Salary Forecast
    |
    v
Business Recommendations
```

---

## Workflow

1. Load the raw student CSV.
2. Clean and enrich the data with engineered features.
3. Save the cleaned dataset for analysis and model training.
4. Build SQL tables, views, and analysis queries.
5. Explore branch-wise, company-wise, and salary-wise trends.
6. Train placement classification and salary regression models.
7. Serve the trained models in Streamlit.
8. Present the insights in a dashboard-friendly format.

---

## Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| Data Cleaning | Python (Pandas) | Deduplication, missing values, feature engineering |
| Data Modeling & Analysis | MySQL (SQL) | Normalized schema, joins, views, analysis queries |
| Visualization | Power BI | KPI cards, dashboards, slicers |
| Machine Learning | Scikit-learn | Placement classification + salary regression |
| Deployment | Streamlit | Live interactive prediction app |

---

## Dataset

- **Size:** 12,000 student records
- **Base columns:** `student_id`, `gender`, `age`, `degree`, `branch`, `cgpa`, `backlogs`, `internships`, `certifications`, `coding_skills`
- **Engineered columns:** `communication_skills`, `project_count`, `internship_status`, `certification_status`, `placement_status`, `package_lpa`, `company_name`, `total_skill_score`, `academic_performance_index`, `employability_score`
- **Outcome split:** 10,937 placed / 1,063 not placed

---

## Screenshots

Existing screenshot assets in the repo:

- `Screen Shots (sql,visualizations)/`
- `PowerBI/`

Suggested screenshots to feature in the README:

- SQL query results
- Power BI executive dashboard
- Placement distribution charts
- Model prediction screen from Streamlit

---

## Dashboard

The Power BI dashboard is designed as an executive placement view with:

- KPI cards for total students, placement rate, average salary, and highest salary
- branch-wise placement breakdown
- gender-wise placement distribution
- company-wise hiring summary
- salary insights by company and branch
- slicers for branch, gender, placement status, and company

This makes it useful for placement officers, department heads, and recruiters.

---

## What This Project Analyzes

**Branch-wise placement** - compares placement rate and salary across AI, CS, DS, Electrical, IT, and Mechanical.

**CGPA and backlogs** - checks whether high CGPA alone is enough or whether backlogs act as a stronger filter.

**Skill impact** - studies internships, certifications, coding, and communication scores against placement outcomes.

**Company analysis** - highlights top recruiters by hire volume and average package.

**Salary distribution** - compares average, top-decile, and highest packages.

---

## SQL Analysis

### Key Results

**Branch Placement Rate**

| Branch | Total | Placed | Rate |
|---|---:|---:|---:|
| Data Science | 1,991 | 1,829 | 91.86% |
| Information Technology | 1,955 | 1,793 | 91.71% |
| Artificial Intelligence | 2,016 | 1,838 | 91.17% |
| Mechanical Engineering | 2,107 | 1,919 | 91.08% |
| Computer Science | 1,950 | 1,772 | 90.87% |
| Electrical Engineering | 1,981 | 1,786 | 90.16% |

**Top Recruiters**

| Company | Hires | Avg Package (LPA) |
|---|---:|---:|
| Infosys | 1,629 | 9.93 |
| Accenture | 1,601 | 9.97 |
| Cognizant | 1,599 | 9.94 |
| Capgemini | 1,558 | 9.92 |
| Adobe | 740 | 13.58 |
| Meta | 751 | 13.56 |
| Amazon | 679 | 13.48 |

Mass recruiters hire in volume around 10 LPA, while product-based companies hire fewer students but pay significantly higher packages.

**Skill and Score Impact**

- Communication score rises from about 75% placement rate at score 2 to about 97% at score 10.
- Average employability score is 11.12 for placed students vs. 8.14 for unplaced students.
- Top packages are concentrated among high-CGPA students with strong skills and internships.
- Students with CGPA above 8 and no placement form a useful intervention list for the placement cell.

*(Full query set, views, stored procedure, and triggers live in `sql_analysis/`.)*

---

## Models

Both trained models are deployed through the Streamlit app.

**Model 1 - Placement Prediction**

- Target: `placement_status`
- Algorithms: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting

**Model 2 - Salary Prediction**

- Target: `package_lpa`
- Algorithms: Linear Regression, Random Forest Regressor, Gradient Boosting Regressor

### Model Workflow

- preprocess student inputs
- predict placement probability
- predict expected salary for placed students
- show the output inside the Streamlit app

---

## Results

- Placement prediction and salary prediction are both available in the app.
- The dataset shows a strong relationship between internships, communication, CGPA, and placement outcome.
- Branch and company breakdowns provide business-level context beyond the raw model output.
- The project is useful both as a prediction demo and as an analytics portfolio piece.

---

## Business Recommendations

- Increase internship participation early in the academic year.
- Run communication and mock interview workshops for at-risk students.
- Prioritize DSA and coding practice for weaker branches.
- Track recruiter-wise hiring patterns to improve company targeting.
- Identify students with low CGPA and backlogs before final-year placement season.
- Use the dashboard in monthly placement review meetings.

---

## Key Insights

- Students with internships show higher placement rates and stronger salary outcomes.
- Communication scores above 7 correlate strongly with better placement outcomes.
- Product-based companies pay more than mass recruiters, but hire fewer students.
- Certifications add measurable value for students with limited experience.
- Employability score is one of the strongest separators between placed and unplaced students.

---

## Project Progress Checklist

| Stage | Status |
|---|---|
| Step 1: Data Cleaning (Python) | Done |
| Step 2: Exploratory Data Analysis (EDA) | Done |
| Step 3: SQL Analysis & Schema | Done |
| Step 4: Power BI Dashboard | Done |
| Step 5: ML - Placement Prediction | Done |
| Step 6: ML - Salary Prediction | Done |
| Business Insights Report | Done |

---

## Project Structure

```text
Placement-Prediction-College-Analytics
|-- data/
|   |-- raw/
|   |-- cleaned/
|-- sql_analysis/
|   |-- schema.sql
|   |-- import.sql
|   |-- cleaning.sql
|   |-- queries.sql
|   |-- views.sql
|-- notebooks/
|-- powerbi/
|-- models/
|-- app.py
|-- README.md
|-- requirements.txt
```

---

## Future Scope

- Finish the Power BI dashboard and connect it to `Branch_Performance` and `Company_Recruitment_Summary`
- Add a student recommendation engine
- Integrate with college ERP or placement cell data
- Add forecasting for year-wise placement trends
- Extend explainability with SHAP-based feature analysis
- Deploy the dashboard with a live hosted database

---

## Author

**Suhani Chauhan**

*Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning*

---

> Disclaimer: Predictions from this project are for educational and analytical purposes only. They do not guarantee actual placement outcomes.

