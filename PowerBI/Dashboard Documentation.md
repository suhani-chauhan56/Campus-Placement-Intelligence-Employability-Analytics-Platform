# 🎓 Placement Prediction & College Analytics Dashboard

An interactive, single-workbook **Power BI** dashboard that analyzes student placement outcomes across branches, companies, and academic performance metrics — built on a cleaned placement dataset of 12,000+ student records.

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Tool](https://img.shields.io/badge/tool-Power%20BI-yellow)
![Data](https://img.shields.io/badge/records-12K%2B-blue)

---

## 📌 Overview

This project explores campus placement data to answer key questions such as:

- What percentage of students get placed, and how does it vary by branch, gender, and CGPA?
- Which companies recruit the most, and what salary packages do they offer?
- How do internships, certifications, and skill scores influence placement outcomes and salary?
- Where do "Placed" vs "Not Placed" students differ most in employability score?

The result is a **3-page Power BI report** — Placement Overview, Student Performance, and Salary Insights — connected through a shared filter panel and consistent color coding.

---

## 🗂️ Dataset

**File:** `placement_data_cleaned.csv`

| Column | Type | Description |
|---|---|---|
| `student_id` | Whole Number | Unique student identifier |
| `age` | Whole Number | Student age |
| `gender` | Text | Male / Female |
| `degree` | Text | Degree pursued |
| `branch` | Text | Engineering branch/specialization |
| `cgpa` | Decimal | Cumulative GPA |
| `backlogs` | Whole Number | Number of academic backlogs |
| `internships` | Whole Number | Number of internships completed |
| `internship_status` | Text | Yes / No |
| `certifications` | Whole Number | Number of certifications earned |
| `certification_status` | Text | Yes / No |
| `coding_skills` | Whole Number | Self/assessed coding skill score |
| `communication_skills` | Whole Number | Communication skill score |
| `project_count` | Whole Number | Number of academic/personal projects |
| `total_skill_score` | Whole Number | Aggregated skill score |
| `academic_performance_index` | Decimal | Composite academic performance index |
| `employability_score` | Decimal | Composite employability rating |
| `has_internship` / `has_certification` | Whole Number | Binary flags (0/1) |
| `placement_status` | Text | Placed / Not Placed |
| `company_name` | Text | Recruiting company (or "Unplaced") |
| `package_lpa` | Decimal | Salary package offered (LPA) |

---

## 🛠️ Tools & Skills Used

- **Power BI Desktop** — data modeling, DAX, visualization
- **Power Query** — data type correction and transformation
- **DAX (Data Analysis Expressions)** — calculated columns and measures
- **SQL** — initial data validation and exploratory querying

---

## 🔧 Build Process

### 1. Data Loading
Data was imported via `Get Data → Text/CSV`, then routed through **Power Query** (not a blind load) to correct column data types:

- **Decimal:** `cgpa`, `package_lpa`, `academic_performance_index`, `employability_score`
- **Whole Number:** `age`, `backlogs`, `internships`, `certifications`, `coding_skills`, `communication_skills`, `project_count`, `total_skill_score`, `has_internship`, `has_certification`
- **Text:** `gender`, `degree`, `branch`, `internship_status`, `certification_status`, `placement_status`, `company_name`

### 2. Calculated Columns

```dax
CGPA_Band =
SWITCH(TRUE(),
    'placement_data_cleaned'[cgpa] < 6, "Below 6",
    'placement_data_cleaned'[cgpa] < 7, "6-7",
    'placement_data_cleaned'[cgpa] < 8, "7-8",
    'placement_data_cleaned'[cgpa] < 9, "8-9",
    "9-10"
)

Placement_Flag = IF('placement_data_cleaned'[placement_status] = "Placed", 1, 0)
```

### 3. DAX Measures

A dedicated **Measures** table holds all report metrics:

```dax
Total Students = COUNTROWS('placement_data_cleaned')

Total Placed = CALCULATE(COUNTROWS('placement_data_cleaned'), 'placement_data_cleaned'[placement_status] = "Placed")

Total Not Placed = [Total Students] - [Total Placed]

Placement Rate = DIVIDE([Total Placed], [Total Students])

Average Salary = CALCULATE(AVERAGE('placement_data_cleaned'[package_lpa]), 'placement_data_cleaned'[placement_status] = "Placed")

Highest Salary = CALCULATE(MAX('placement_data_cleaned'[package_lpa]), 'placement_data_cleaned'[placement_status] = "Placed")

Average CGPA = AVERAGE('placement_data_cleaned'[cgpa])

Internship Participation Rate =
DIVIDE(
    CALCULATE(COUNTROWS('placement_data_cleaned'), 'placement_data_cleaned'[internship_status] = "Yes"),
    [Total Students]
)

Avg Employability (Placed) = CALCULATE(AVERAGE('placement_data_cleaned'[employability_score]), 'placement_data_cleaned'[placement_status] = "Placed")

Avg Employability (Not Placed) = CALCULATE(AVERAGE('placement_data_cleaned'[employability_score]), 'placement_data_cleaned'[placement_status] = "Not Placed")

Total Recruiters = CALCULATE(DISTINCTCOUNT('placement_data_cleaned'[company_name]), 'placement_data_cleaned'[company_name] <> "Unplaced")
```

### 4. Formatting Conventions
- `Placement Rate` and `Internship Participation Rate` formatted as **Percentage**
- `Average Salary` / `Highest Salary` formatted as **Decimal (2 places)** with a custom `0.00" LPA"` suffix
- A single consistent color theme is applied throughout: **blue = Placed**, **muted gray/dark = Not Placed**, so trends are visually traceable across every chart
- Tooltips on the CGPA vs. Package scatter chart show `student_id` and `cgpa` on hover

---

## 📊 Dashboard Pages

### 1️⃣ Placement Overview

KPI strip (Total Students, Placement Rate, Average Salary, Highest Salary, Internship Participation Rate, Average CGPA) plus branch-wise and company-wise placement breakdowns, a Placed vs. Not Placed donut, and a gender-split stacked bar.

![Placement Overview](./screenshots/placement-overview.png)

**Visuals included:**
| Visual | Axis | Values |
|---|---|---|
| Clustered column | `branch` | Placement Rate |
| Donut chart | `placement_status` | Total Students |
| Stacked bar | `gender` | Sum of `Placement_Flag`, legend = `placement_status` |
| Bar chart (Top 10) | `company_name` (excl. "Unplaced") | Count of hires |

---

### 2️⃣ Student Performance

Examines how academic and skill metrics correlate with placement outcomes and salary.

![Student Performance](./screenshots/student-performance.png)

**Visuals included:**
| Visual | Axis | Values |
|---|---|---|
| Column chart | `CGPA_Band` | Placement Rate |
| Scatter chart | X = `cgpa`, Y = `package_lpa` | Legend = `branch`, filtered to Placed |
| Column chart | `communication_skills` | Placement Rate |
| Column chart | `internships` | Average Salary |
| Clustered column | `placement_status` | Avg Employability (Placed) vs. (Not Placed) |

---

### 3️⃣ Salary Insights

Deep dive into compensation trends by branch and recruiter, with a full heatmap matrix and top-package student table.

![Salary Insights](./screenshots/salary-insights.png)

**Visuals included:**
| Visual | Axis | Values |
|---|---|---|
| Bar chart | `branch` | Average Salary |
| Bar chart | `company_name` (excl. "Unplaced") | Average Salary |
| Table | `student_id`, `cgpa`, `branch`, `company_name`, `package_lpa` | Sorted by package, Top 10 |
| Matrix (heatmap) | Rows = `branch`, Columns = `company_name` | Count / Salary values |

---

### 🎛️ Global Filters (Slicer Panel)

Available across pages for cross-filtering:
`branch` · `gender` · `placement_status` · `company_name` · `cgpa` (range slider) · `internships`

---

## 💡 Key Insights

- Overall placement rate stands at **~91%**, with **~9%** of students remaining unplaced.
- Placement likelihood rises consistently with **CGPA band** — the 9-10 band shows the highest placement rate, tapering down toward "Below 6".
- **Internship count** shows a clear positive relationship with average salary offered.
- **Average employability score** is consistently higher among placed students than unplaced ones.
- High-paying offers are concentrated among a small set of top recruiters (e.g., Google, Meta, Microsoft), while volume hiring is dominated by mass recruiters like Infosys, TCS, and Accenture.

---

## 🚀 How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/suhani-chauhan56/Placement-Prediction-College-Analytics.git
   ```
2. Open `dashboard/Placement_Analytics_Dashboard.pbix` in **Power BI Desktop**.
3. If prompted, update the data source path to point to `data/placement_data_cleaned.csv` on your machine.
4. Use the slicer panel on each page to filter by branch, gender, company, CGPA range, or internship count.

---

## 👤 Author

**Suhani Chauhan**
GitHub: [@suhani-chauhan56](https://github.com/suhani-chauhan56)

---

## 📄 License

This project is open-sourced for educational and portfolio purposes. Feel free to fork and adapt with attribution.
