<div align="center">

# 🎓 Placement-Prediction-College-Analytics

### 🚀 Placement analytics, SQL insights, dashboards, and ML prediction in one project

**Python** -> **MySQL** -> **Power BI** -> **Machine Learning**

![Python](https://img.shields.io/badge/Python-Pandas%20%7C%20Sklearn-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Partially%20Complete-yellow?style=for-the-badge)

### 🌟 [Live Demo - Try the Prediction App](https://placement-prediction-college-analytics-j7evnb2vmmmjxmnc6g4fdq.streamlit.app/)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://placement-prediction-college-analytics-j7evnb2vmmmjxmnc6g4fdq.streamlit.app/)

</div>

---

This project turns raw placement data into a practical analytics product. It combines ETL, SQL analysis, EDA, executive dashboarding, ML prediction, explainability, and decision support in one repo.

---

## 📌 Business Problem

The placement cell needs a faster way to answer:

- Which branches are performing best?
- Which recruiters hire the most students?
- Which students need early intervention?
- How do internships and skills affect placement outcomes?
- What is the expected salary for a student profile?

---

## 🧭 Final Architecture

```text
Student Data
    │
    ▼
ETL Pipeline (Python + SQL)
    │
    ▼
Data Warehouse
    │
    ▼
EDA
    │
    ▼
Power BI Executive Dashboard
    │
    ▼
ML Placement Prediction
    │
    ▼
SHAP Explainability
    │
    ▼
Student Risk Score
    │
    ▼
Personalized Recommendations
    │
    ▼
Placement Officer Dashboard
```

---

## 🛠️ Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| Data Cleaning | Python (Pandas) | Deduplication, missing values, feature engineering |
| Data Modeling & Analysis | MySQL (SQL) | Normalized schema, joins, views, analysis queries |
| Visualization | Power BI | KPI cards, dashboards, slicers |
| Machine Learning | Scikit-learn | Placement classification + salary regression |
| Deployment | Streamlit | Live interactive prediction app |

---

## 🧱 ETL Pipeline

```text
Raw CSV
   ↓
Cleaning
   ↓
Transformation
   ↓
Feature Engineering
   ↓
SQL Database
   ↓
Python Analytics
   ↓
Power BI
```

---

## 📊 Dataset

- **Size:** 12,000 student records
- **Base columns:** `student_id`, `gender`, `age`, `degree`, `branch`, `cgpa`, `backlogs`, `internships`, `certifications`, `coding_skills`
- **Engineered columns:** `communication_skills`, `project_count`, `internship_status`, `certification_status`, `placement_status`, `package_lpa`, `company_name`, `total_skill_score`, `academic_performance_index`, `employability_score`
- **Outcome split:** 10,937 placed / 1,063 not placed

---

## 📸 Screenshots

Existing assets in the repo:

- `Screen Shots (sql,visualizations)/`
- `PowerBI/`

Use them to showcase:

- SQL query results
- Power BI executive dashboard
- Placement charts
- Streamlit prediction screen

---

## 📈 Dashboard

The Power BI and Streamlit views focus on executive placement reporting:

- KPI cards for total students, placement rate, average salary, and highest salary
- branch-wise placement breakdown
- gender-wise placement distribution
- company-wise hiring summary
- salary insights by branch and recruiter
- slicers for branch, gender, placement status, and company

The Streamlit app also includes:

- placement prediction
- salary estimation
- student risk score
- explanation panel
- improvement recommendations
- department dashboard

---

## 🗃️ SQL Analysis

Recruiters love SQL because it shows practical analytics thinking.

### Example analyses

- Top 10 companies hiring
- Branch with highest package
- Average CGPA by company
- Students with internship but no placement
- Placement rate by gender
- Package distribution
- Students requiring intervention

### Why SQL matters

- It demonstrates data modeling, joins, grouping, and reporting.
- It supports dashboard refreshes and executive reporting.
- It creates reusable analysis for placement-cell reviews.

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

---

## 🤖 Models

**Placement Prediction**

- Target: `placement_status`
- Algorithms: Logistic Regression, Decision Tree, Random Forest

**Salary Prediction**

- Target: `package_lpa`
- Algorithms: Linear Regression

### Workflow

- preprocess student inputs
- predict placement probability
- estimate expected salary
- show the output inside the Streamlit app

---

## 🎯 Student Risk Score

Instead of only showing:

- Placed
- Not Placed

The project also shows:

- Employability Score
- Placement Risk
- Recommendation

This turns the app into decision support, not just prediction.

---

## 🧠 SHAP Explainability

The app explains the main factors behind a prediction, such as:

- CGPA `+18%`
- Internship `+15%`
- Communication `+12%`
- Coding `-8%`
- Projects `-10%`

This makes the output easier to trust and discuss.

---

## ✅ Results

- Placement prediction and salary prediction are both available in the app.
- The dataset shows a strong relationship between internships, communication, CGPA, and placement outcome.
- Branch and company analytics give the project a real placement-office feel.

---

## 💡 Business Recommendations

- Increase internship participation early in the academic year.
- Run communication and mock interview workshops for at-risk students.
- Prioritize DSA and coding practice for weaker branches.
- Track recruiter-wise hiring patterns to improve company targeting.
- Identify students with low CGPA and backlogs before final-year placement season.
- Prioritize departments with declining placement trends.

---

## ⭐ Key Insights

- Students with internships show higher placement rates and stronger salary outcomes.
- Communication scores above 7 correlate strongly with better placement outcomes.
- Product-based companies pay more than mass recruiters, but hire fewer students.
- Certifications add measurable value for students with limited experience.
- Employability score is one of the strongest separators between placed and unplaced students.

---

## 🧾 Project Progress Checklist

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

## 🗂️ Project Structure

```text
Placement-Prediction-College-Analytics
|-- data/
|   |-- raw/
|   |-- cleaned/
|   |-- marts/
|-- sql_analysis/
|   |-- schema.sql
|   |-- import.sql
|   |-- cleaning.sql
|   |-- queries.sql
|   |-- views.sql
|-- sql/
|   |-- placement_flat_table.csv
|-- notebooks/
|-- powerbi/
|-- models/
|-- app.py
|-- README.md
|-- requirements.txt
```

---

## 🚀 Deployment

The project can be tested or deployed with:

- Streamlit
- Render
- Azure
- Hugging Face Spaces

---

## 🚀 Future Scope

- Expand the Power BI dashboard into a more complete placement officer view
- Add a stronger recommendation engine
- Integrate with college ERP or placement cell data
- Add forecasting for year-wise placement trends
- Extend explainability with SHAP-based feature analysis

---

## 👩‍💻 Author

**Suhani Chauhan**

*Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning*

---

> Disclaimer: Predictions from this project are for educational and analytical purposes only. They do not guarantee actual placement outcomes.
