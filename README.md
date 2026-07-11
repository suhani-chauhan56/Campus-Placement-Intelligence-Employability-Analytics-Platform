# 🎓 Placement Prediction & College Analytics

### Turning student academic & skill data into placement predictions and salary insights

**Python** → **MySQL** → **Power BI** → **Machine Learning**

![Python](https://img.shields.io/badge/Python-Pandas%20%7C%20Sklearn-3776AB?style=for-the-badge&logo=python&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) ![Status](https://img.shields.io/badge/Status-Complete-yellow?style=for-the-badge)

### 🚀 [**LIVE DEMO — Try the Prediction App**](https://placement-prediction-college-analytics-j7evnb2vmmmjxmnc6g4fdq.streamlit.app/)

---

Every placement season, colleges sit on a goldmine of data — CGPA, internships, certifications, coding and communication scores — but rarely turn it into a system that actually predicts outcomes.

This project builds an end-to-end **Placement Analytics & Prediction system**: clean the raw student dataset, model it in SQL, explore what actually drives placements, visualize it in Power BI, and predict **placement likelihood** and **expected salary** with machine learning.

---

## 🧾 Executive Summary

> Analyzed **12,000 student records** — academics, skills, and placement outcomes across 6 branches and 13 recruiting companies — to find what drives campus placements, and built classification & regression models to predict **Placement Status** and **Expected Package (LPA)**.

---

## 🏗️ Architecture

```
📄 Raw Student Dataset (12,000 records)
     │
     ▼
🧹 PYTHON (Pandas) — Data Cleaning
     │   (dedupe, missing values, feature engineering)
     ▼
🗃️ SQL (MySQL) — Modeling & Analysis
     │   (normalized schema, branch/company/salary queries, views, triggers)
     ▼
📊 POWER BI — Visualization
     │   (KPI cards, dashboards, interactive slicers)
     ▼
🤖 MACHINE LEARNING — Prediction Layer
     │   (Placement classification + Salary regression)
     ▼
💡 INSIGHTS LAYER — Business Decisions
     (recruiter targeting · at-risk students · branch strategy)
```

---

## 🧰 Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| 🧹 Data Cleaning | **Python (Pandas)** | Deduplication, missing values, feature engineering |
| 🗃️ Data Modeling & Analysis | **MySQL (SQL)** | Normalized schema, joins, window functions, CTEs, views, triggers |
| 📊 Visualization | **Power BI** | KPI cards, multi-dashboard reporting, slicers |
| 🤖 Machine Learning | **Scikit-learn** | Placement classification + salary regression |

---

## 📁 Dataset

- **Size:** 12,000 student records, 22 columns
- **Fields:** `student_id`, `gender`, `age`, `degree`, `branch`, `cgpa`, `backlogs`, `internships`, `certifications`, `coding_skills`, `communication_skills`, `project_count`, `placement_status`, `package_lpa`, `company_name`, plus engineered features (`total_skill_score`, `academic_performance_index`, `employability_score`)
- **Outcome split:** 10,937 placed / 1,063 not placed — **91.14%** overall placement rate

---

## 🔍 What This Project Analyzes

**Branch-wise Placement** — comparing placement rates and average packages across AI, CS, DS, Electrical, IT, and Mechanical.

**CGPA & Backlogs vs. Placement** — whether high CGPA alone guarantees placement, or if backlog count is a harder filter.

**Skill Impact** — internship count, certifications, and coding/communication scores against placement rate and package.

**Company Analysis** — top recruiting companies by hire volume and average package, and which companies favor which branches.

**Salary Distribution** — average, top-decile, and highest packages across the dataset.

---

## 📊 SQL Analysis — Key Results

**Branch Placement Rate**
| Branch | Total | Placed | Rate |
|---|---|---|---|
| Data Science | 1,991 | 1,829 | **91.86%** |
| Information Technology | 1,955 | 1,793 | 91.71% |
| Artificial Intelligence | 2,016 | 1,838 | 91.17% |
| Mechanical Engineering | 2,107 | 1,919 | 91.08% |
| Computer Science | 1,950 | 1,772 | 90.87% |
| Electrical Engineering | 1,981 | 1,786 | 90.16% |

**Top Recruiters**
| Company | Hires | Avg Package (LPA) |
|---|---|---|
| Infosys | 1,629 | 9.93 |
| Accenture | 1,601 | 9.97 |
| Cognizant | 1,599 | 9.94 |
| Capgemini | 1,558 | 9.92 |
| Adobe | 740 | 13.58 |
| Meta | 751 | 13.56 |
| Amazon | 679 | 13.48 |

Mass recruiters hire in volume around ~10 LPA; product-based companies hire far fewer but pay 35–40% more.

**Skill & Score Impact**
- Communication score climbs from ~75% placement rate at score 2 to ~97% at score 10 — a near-linear relationship.
- Avg employability score: **11.12 for placed vs. 8.14 for unplaced** — the clearest separator in the data.
- Top packages (17.2–17.7 LPA) go to CGPA 9.3+ students placed at Adobe, Meta, Microsoft, and Amazon.
- Only **76 students** have CGPA > 8 and are still unplaced — a short, specific follow-up list for the placement cell.

*(Full query set, views, stored procedure, and triggers live in `sql_analysis/`.)*

---

## 📊 Dashboard Features (Power BI) 🟡 In Progress

🔲 KPI Cards — Total Students, Placement Rate, Average Salary, Highest Salary, Internship Participation, Average CGPA
🔲 **Dashboard 1 — Placement Overview:** placement by branch, gender, company-wise recruitment
🔲 **Dashboard 2 — Student Performance:** CGPA distribution, skill impact, communication scores
🔲 **Dashboard 3 — Salary Insights:** salary by branch, company, CGPA, top recruiters
🔲 **Dashboard 4 — Interactive Filters:** slicers for branch, gender, placement status, company, CGPA range

---

## 🤖 Machine Learning Models ✅ Completed

> 🚀 **Live Demo:** [**Open the Streamlit App →**](https://placement-prediction-college-analytics-j7evnb2vmmmjxmnc6g4fdq.streamlit.app/) Enter student details to get a real-time **Placement Prediction** and **Expected Salary (LPA)** estimate.
>
> ⚠️ *This is a prediction based on historical trends, not a guarantee — real outcomes depend on each company's own hiring criteria.*

**Model 1 — Placement Prediction (Classification)**
- Target: `placement_status`
- Algorithms: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting

**Model 2 — Salary Prediction (Regression)**
- Target: `package_lpa`
- Algorithms: Linear Regression, Random Forest Regressor, Gradient Boosting Regressor

---

## 💡 Key Insights

- 🎓 Students with internships show meaningfully higher placement rates and packages than those without.
- 🗣️ Communication scores above ~7 correlate strongly with better placement outcomes (up to 97% placement rate at score 10).
- 💰 Product-based companies (Adobe, Meta, Amazon) pay 35–40% more than mass recruiters, but hire in far smaller numbers.
- 📜 Certifications add measurable salary lift even for students with zero internships.
- 🧠 Employability score is the single strongest separator between placed and unplaced students (11.12 vs. 8.14 avg).

---

## ✅ Project Progress Checklist

| Stage | Status |
|---|---|
| Step 1: Data Cleaning (Python) | ✅ Done |
| Step 2: Exploratory Data Analysis (EDA) | ✅ Done |
| Step 3: SQL Analysis & Schema | ✅ Done |
| Step 4: Power BI Dashboard | 🟡 In Progress |
| Step 5: ML — Placement Prediction | ✅ Done |
| Step 5: ML — Salary Prediction | ✅ Done |
| Business Insights Report | ✅ Done |

---

## 🗂️ Project Structure

```
📦 Placement-Prediction-College-Analytics
 ┣ 📂 data/
 ┃ ┣ 📂 raw/
 ┃ ┗ 📂 cleaned/
 ┃    ┗ 📜 placement_data_cleaned.csv
 ┣ 📂 sql_analysis/
 ┃ ┣ 📜 schema.sql
 ┃ ┣ 📜 import.sql
 ┃ ┣ 📜 cleaning.sql
 ┃ ┣ 📜 queries.sql
 ┃ ┣ 📜 views.sql
 ┣ 📂 notebooks/
 ┃ ┣ 📓 data_cleaning.ipynb
 ┃ ┣ 📓 eda.ipynb
 ┃ ┗ 📓 model_training.ipynb
 ┣ 📂 powerbi/
 ┃ ┗ 📊 Placement_Dashboard.pbix
 ┣ 📂 models/
 ┃ ┣ 🤖 placement_model.pkl
 ┃ ┗ 🤖 salary_model.pkl
 ┣ 📄 app.py
 ┣ 📄 README.md
 ┗ 📄 requirements.txt
```

---

## 🚀 Future Improvements

- 📊 Finish the Power BI dashboard and connect it to `Branch_Performance` / `Company_Recruitment_Summary` views
- 🎯 Skill-gap recommendation engine for students
- 🔌 Live integration with college ERP/placement cell data
- 🧠 Deep learning-based placement prediction

---

## 👩‍💻 Author

**Suhani Chauhan**

*Aspiring Data Analyst | Python • SQL • Power BI • Machine Learning*

---

⭐ **This project is still being built — star/watch the repo to follow progress!**

> ⚠️ **Disclaimer:** Predictions from this project are for educational and analytical purposes only. They do not guarantee actual placement outcomes.
