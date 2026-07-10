<div align="center">

# 🎓 Placement Prediction & College Analytics

### Turning student academic & skill data into placement predictions and salary insights

**Python** → **MySQL** → **Power BI** → **Machine Learning**

![Python](https://img.shields.io/badge/Python-Pandas%20%7C%20Sklearn-3776AB?style=for-the-badge&logo=python&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) ![Status](https://img.shields.io/badge/Status-Partially%20Complete-yellow?style=for-the-badge)

### 🚀 [**LIVE DEMO — Try the Prediction App**](https://placement-prediction-college-analytics-j7evnb2vmmmjxmnc6g4fdq.streamlit.app/)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://placement-prediction-college-analytics-j7evnb2vmmmjxmnc6g4fdq.streamlit.app/)

</div>

---

Every placement season, colleges sit on a goldmine of data — CGPA, internships, certifications, aptitude scores, communication ratings — but rarely turn it into a system that actually predicts outcomes.

This project builds an end-to-end **Placement Analytics & Prediction system**: clean the raw student dataset, explore what actually drives placements, model it in SQL, visualize it in Power BI, and finally predict **placement likelihood** and **expected salary** using machine learning.

> ⚠️ **Project Status: Partially Complete**
> Data cleaning, EDA, and both ML models (placement prediction + salary prediction) are **done**. SQL analysis and the Power BI dashboard are **in progress**. See checklist below for details.

---

## 🧾 Executive Summary

> Analyzing student academic performance, skills, and internship/certification history to understand what drives campus placements — and building classification & regression models to predict **Placement Status** and **Expected Package (LPA)**.

---

## 🏗️ Architecture

```
📄 Raw Student Dataset (5,000–20,000 records)
     │
     ▼
🧹 PYTHON (Pandas) — Data Cleaning
     │   (dedupe, missing values, outliers, encoding, feature engineering)
     ▼
🗃️ SQL (MySQL) — Modeling & Analysis
     │   (normalized tables, department/company/salary queries)
     ▼
📊 POWER BI — Visualization
     │   (KPI cards, 4 dashboards, interactive slicers)
     ▼
🤖 MACHINE LEARNING — Prediction Layer
     │   (Placement classification + Salary regression)
     ▼
💡 INSIGHTS LAYER — Business Decisions
     (skill gaps · department strategy · recruiter targeting)
```

---

## 🧰 Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| 🧹 Data Cleaning | **Python (Pandas)** | Deduplication, missing values, outlier handling, encoding, derived features |
| 🗃️ Data Modeling & Analysis | **MySQL (SQL)** | Normalized schema, aggregation queries, eligibility checks |
| 📊 Visualization | **Power BI** | KPI cards, multi-dashboard reporting, slicers |
| 🤖 Machine Learning | **Scikit-learn** | Placement classification + salary regression |
| 📈 EDA & Plotting | **Matplotlib, Plotly** | Distribution, correlation, and trend visualizations |

---

## 📁 Dataset

- 📦 **Size:** 5,000–20,000 synthetic/real student placement records
- 📊 **Fields:** Student_ID, Gender, Age, Department, CGPA, Attendance, Aptitude_Score, Technical_Score, Communication_Score, Internship, Projects, Certifications, Hackathons, Backlogs, Placement_Status, Company, Package_LPA
- 🔗 **Source:** Kaggle / custom-collected college placement dataset *(link to be added)*

---

## 🔍 What This Project Analyzes

### 📈 Overall Placement Rate
Total students, total placed, and overall placement percentage.

### 🏫 Department-wise Placement
Comparing placement rates across CSE, IT, ECE, Mechanical, and other departments.

### 🎓 CGPA vs Placement
Does a higher CGPA always guarantee placement? Is there a minimum threshold? (Scatter & box plots)

### 💼 Internship Impact
Placement rate comparison between students with and without internship experience.

### 📜 Certifications Analysis
Whether certification count correlates with better placement outcomes.

### 🗣️ Communication Skills
Impact of communication scores on placement likelihood.

### 🛠️ Project Count Analysis
Relationship between number of projects completed and salary offered.

### 💰 Salary Distribution
Average, median, and highest package analysis (histogram & box plot).

### 🏢 Company Analysis
Top recruiting companies by number of hires and average package offered.

---

## 📊 Dashboard Features (Power BI) 🟡 In Progress

✅ KPI Cards — Total Students, Placement Rate, Average Salary, Highest Salary, Internship Participation, Average CGPA
✅ **Dashboard 1 — Placement Overview:** placement by department, gender, trend over time, company-wise recruitment
✅ **Dashboard 2 — Student Performance:** CGPA distribution, certification analysis, internship impact, communication scores
✅ **Dashboard 3 — Salary Insights:** salary by department, company, CGPA, top recruiters
✅ **Dashboard 4 — Interactive Filters:** slicers for department, gender, batch, placement status, company, internship, CGPA range

---

## 🤖 Machine Learning Models ✅ Completed

> 🚀 **Live Demo:** [**Open the Streamlit App →**](https://placement-prediction-college-analytics-j7evnb2vmmmjxmnc6g4fdq.streamlit.app/)
> Enter student details (CGPA, internships, projects, scores, etc.) to get a real-time **Placement Prediction** and **Expected Salary (LPA)** estimate.
>
> ⚠️ *Note: This is only a **prediction** based on historical data trends — it is not a guarantee of placement. Real-world outcomes depend on each company's own hiring criteria, interview process, and requirements.*

### Model 1 — Placement Prediction (Classification)
- **Target:** `Placement_Status`
- **Algorithms:** Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost (optional)
- **Metrics:** Accuracy, Precision, Recall, F1 Score, ROC-AUC
- **Expected Accuracy:** ~85–92% (dataset dependent)

### Model 2 — Salary Prediction (Regression)
- **Target:** `Package_LPA`
- **Algorithms:** Linear Regression, Random Forest Regressor, Gradient Boosting Regressor
- **Metrics:** RMSE, MAE, R² Score

---

## 💡 Key Insights *(to be validated once modeling is complete)*

- 🎓 Students with internships are expected to show significantly higher placement rates.
- 🗣️ Communication scores above a certain threshold may correlate with better placement outcomes.
- 🛠️ Departments with more project-based learning may achieve higher average salaries.
- 📜 Students with multiple certifications tend to receive better salary offers.
- 🧠 Higher aptitude scores often align with placements in product-based companies.

---

## ✅ Project Progress Checklist

| Stage | Status |
|---|---|
| Step 1: Data Cleaning (Python) | ✅ Done |
| Step 2: Exploratory Data Analysis (EDA) | ✅ Done |
| Step 3: SQL Analysis & Schema | 🟡 In Progress |
| Step 4: Power BI Dashboard | 🟡 In Progress |
| Step 5: ML — Placement Prediction | ✅ Done |
| Step 5: ML — Salary Prediction | ✅ Done |
| Business Insights Report | 🔲 Not Started |
| Final Documentation & README polish | 🔲 Not Started |

> 📝 Update the checkboxes above as each stage is completed (🔲 → ✅).

---

## 🗂️ Project Structure

```
📦 Placement-Prediction-Analytics
 ┣ 📂 data/
 ┃ ┣ 📂 raw/
 ┃ ┗ 📂 cleaned/
 ┣ 📂 sql/
 ┃ ┣ 📜 schema.sql
 ┃ ┣ 📜 queries.sql
 ┃ ┗ 📜 views.sql
 ┣ 📂 notebooks/
 ┃ ┣ 📓 data_cleaning.ipynb
 ┃ ┣ 📓 eda.ipynb
 ┃ ┗ 📓 model_training.ipynb
 ┣ 📂 powerbi/
 ┃ ┗ 📊 Placement_Dashboard.pbix
 ┣ 📂 models/
 ┃ ┣ 🤖 placement_model.pkl
 ┃ ┗ 🤖 salary_model.pkl
 ┣ 📂 reports/
 ┃ ┗ 📄 insights.pdf
 ┣ 📂 images/
 ┃ ┣ 🖼️ dashboard.png
 ┃ ┗ 🖼️ confusion_matrix.png
 ┣ 📄 README.md
 ┗ 📄 requirements.txt
```

---

## 🚀 Future Improvements

- 🧠 Deep learning-based placement prediction
- 🌐 Deploy models as a web app (Flask/Streamlit)
- 🔌 Live integration with college ERP/placement cell data
- 📊 Automated Power BI refresh pipeline
- 🎯 Skill-gap recommendation engine for students

---

## 👩‍💻 Author

**Suhani Chauhan**

*Aspiring Data Analyst | Python • SQL • Power BI • Machine Learning*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](#) [![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](#)

---

⭐ **This project is still being built — star/watch the repo to follow progress!**

*A portfolio project demonstrating end-to-end data analytics: cleaning, SQL, dashboarding, and machine learning applied to campus placements.*

> ⚠️ **Disclaimer:** The predictions generated by this project are for **educational and analytical purposes only**. They do not guarantee a student's actual placement — real placement outcomes are ultimately decided by each **recruiting company's own criteria**.
