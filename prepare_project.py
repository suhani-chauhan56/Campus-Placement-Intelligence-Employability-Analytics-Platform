from __future__ import annotations

import json
import os
import pickle
import shutil
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier


ROOT = Path(__file__).resolve().parent
RAW_SOURCE = ROOT / "Indian_Student_Placement_Dataset_2025-selected-columns.csv"
RAW_DEST = ROOT / "data" / "raw" / RAW_SOURCE.name
CLEANED_PATH = ROOT / "data" / "cleaned" / "placement_data_cleaned.csv"
MARTS_DIR = ROOT / "data" / "marts"
MODELS_DIR = ROOT / "models"
REPORTS_DIR = ROOT / "reports"


def ensure_directories() -> None:
    """Create the project folders used by ETL, analytics, and model artifacts."""
    folders = [
        ROOT / "data" / "raw",
        ROOT / "data" / "cleaned",
        ROOT / "data" / "marts",
        ROOT / "sql",
        ROOT / "notebooks",
        ROOT / "models",
        ROOT / "dashboard",
        ROOT / "images",
        ROOT / "reports",
        ROOT / "app",
    ]
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
        print(f"Ensured directory: {folder.relative_to(ROOT)}")


def setup_project() -> None:
    """Prepare the workspace and stage the raw source data."""
    print("=== Step 1: Setting up project structure ===")
    ensure_directories()

    if RAW_SOURCE.exists():
        shutil.copy2(RAW_SOURCE, RAW_DEST)
        print(f"Copied raw dataset to: {RAW_DEST.relative_to(ROOT)}")
    else:
        print(f"Warning: {RAW_SOURCE.name} not found in workspace root.")


def _generate_recommendations(row: pd.Series) -> str:
    recommendations: list[str] = []

    if row["backlogs"] > 0:
        recommendations.append("Clear backlogs early")
    if row["cgpa"] < 7.0:
        recommendations.append("Raise CGPA above 7.0")
    if row["internships"] == 0:
        recommendations.append("Complete an internship")
    if row["coding_skills"] < 6:
        recommendations.append("Improve DSA and coding practice")
    if row["communication_skills"] < 6:
        recommendations.append("Strengthen communication skills")
    if row["project_count"] < 2:
        recommendations.append("Build more portfolio projects")
    if row["certifications"] == 0:
        recommendations.append("Add one industry certification")

    if not recommendations:
        return "Profile is competitive; keep building projects and interview readiness"

    return "; ".join(recommendations[:3])


def _risk_band(score: float) -> str:
    if score <= 35:
        return "Low"
    if score <= 65:
        return "Medium"
    return "High"


def enrich_data() -> pd.DataFrame | None:
    """Create synthetic analytics fields and the target labels used downstream."""
    print("\n=== Step 2: Enriching raw data with analytics columns ===")
    raw_path = RAW_DEST if RAW_DEST.exists() else RAW_SOURCE
    if not raw_path.exists():
        print("Error: raw dataset not found. Cannot continue.")
        return None

    df = pd.read_csv(raw_path)
    print(f"Loaded raw data with shape: {df.shape}")

    np.random.seed(42)
    n_records = len(df)

    df["communication_skills"] = np.clip(np.round(np.random.normal(6.5, 1.5, n_records)), 1, 10).astype(int)
    df["project_count"] = [
        int(np.clip(np.random.poisson(max(0.5, coding_val / 2.0)), 0, 5))
        for coding_val in df["coding_skills"]
    ]
    df["internship_status"] = np.where(df["internships"] > 0, "Yes", "No")
    df["certification_status"] = np.where(df["certifications"] > 0, "Yes", "No")

    df["placement_year"] = 2019 + ((df["student_id"] - 1) % 6)

    log_odds = (
        1.6 * (df["cgpa"] - 6.0)
        + 0.5 * df["coding_skills"]
        + 0.4 * df["communication_skills"]
        + 0.8 * df["internships"]
        + 0.6 * df["project_count"]
        - 1.2 * df["backlogs"]
        - 3.5
    )
    prob = 1 / (1 + np.exp(-log_odds))
    df["placement_status"] = np.where(np.random.binomial(1, prob), "Placed", "Not Placed")

    package_values = []
    for _, row in df.iterrows():
        if row["placement_status"] == "Placed":
            package = (
                3.5
                + 0.9 * (row["cgpa"] - 6.0)
                + 0.45 * row["coding_skills"]
                + 0.7 * row["internships"]
                + 0.5 * row["project_count"]
                + 0.3 * row["certifications"]
                + np.random.normal(0, 0.6)
            )
            package_values.append(max(3.0, round(float(package), 2)))
        else:
            package_values.append(0.0)
    df["package_lpa"] = package_values

    high_tier = ["Google", "Microsoft", "Amazon", "Adobe", "Meta"]
    mid_tier = ["Accenture", "Capgemini", "Cognizant", "Infosys"]
    low_tier = ["TCS", "Wipro", "Tech Mahindra"]

    company_values = []
    for _, row in df.iterrows():
        if row["placement_status"] == "Placed":
            pkg = row["package_lpa"]
            if pkg >= 12.0:
                company_values.append(np.random.choice(high_tier))
            elif pkg >= 7.5:
                company_values.append(np.random.choice(mid_tier))
            else:
                company_values.append(np.random.choice(low_tier))
        else:
            company_values.append("Unplaced")
    df["company_name"] = company_values

    print(f"Enriched dataset shape: {df.shape}")
    print(df["placement_status"].value_counts().to_string())
    return df


def clean_and_process_data(df: pd.DataFrame | None) -> pd.DataFrame | None:
    """Standardize the enriched dataset and build analytic features."""
    print("\n=== Step 3: Cleaning and feature engineering ===")
    if df is None:
        return None

    cleaned = df.copy()

    duplicate_count = cleaned.duplicated().sum()
    if duplicate_count:
        cleaned = cleaned.drop_duplicates()
        print(f"Removed {duplicate_count} duplicate records.")
    else:
        print("No duplicate records found.")

    if cleaned.isnull().any().any():
        before_rows = len(cleaned)
        cleaned = cleaned.dropna().copy()
        print(f"Dropped rows with missing values: {before_rows - len(cleaned)}")
    else:
        print("No missing values found.")

    branch_map = {
        "CS": "Computer Science",
        "IT": "Information Technology",
        "Electrical": "Electrical Engineering",
        "Mechanical": "Mechanical Engineering",
        "DS": "Data Science",
        "AI": "Artificial Intelligence",
    }
    cleaned["branch"] = cleaned["branch"].replace(branch_map)

    cleaned["has_internship"] = cleaned["internship_status"].map({"Yes": 1, "No": 0}).astype(int)
    cleaned["has_certification"] = cleaned["certification_status"].map({"Yes": 1, "No": 0}).astype(int)

    cleaned["total_skill_score"] = cleaned["coding_skills"] + cleaned["communication_skills"]
    cleaned["academic_performance_index"] = (cleaned["cgpa"] * 10) - (cleaned["backlogs"] * 5)
    cleaned["employability_score"] = (
        cleaned["total_skill_score"] * 0.4
        + cleaned["cgpa"] * 0.4
        + cleaned["internships"] * 2.0
        + cleaned["project_count"] * 1.2
        + cleaned["certifications"] * 0.8
        - cleaned["backlogs"] * 1.5
    ).round(2)

    placement_risk = (
        100
        - (cleaned["cgpa"] * 6.0)
        - (cleaned["coding_skills"] * 4.0)
        - (cleaned["communication_skills"] * 3.0)
        - (cleaned["internships"] * 8.0)
        - (cleaned["project_count"] * 4.0)
        - (cleaned["certifications"] * 2.0)
        + (cleaned["backlogs"] * 12.0)
    )
    cleaned["placement_risk_score"] = placement_risk.clip(0, 100).round(1)
    cleaned["risk_band"] = cleaned["placement_risk_score"].apply(_risk_band)
    cleaned["student_intervention"] = cleaned.apply(_generate_recommendations, axis=1)
    cleaned["intervention_priority"] = np.where(
        cleaned["risk_band"].eq("High"),
        "Immediate",
        np.where(cleaned["risk_band"].eq("Medium"), "Monitor", "Track"),
    )
    cleaned["eligible_for_shortlist"] = ((cleaned["cgpa"] >= 6.5) & (cleaned["backlogs"] == 0)).astype(int)

    cleaned.to_csv(CLEANED_PATH, index=False)
    print(f"Cleaned dataset saved to: {CLEANED_PATH.relative_to(ROOT)}")

    save_analytics_marts(cleaned)
    save_sql_summaries(cleaned)
    return cleaned


def save_analytics_marts(df: pd.DataFrame) -> None:
    """Write CSV marts for Power BI and departmental reporting."""
    MARTS_DIR.mkdir(parents=True, exist_ok=True)

    branch_summary = (
        df.groupby("branch", as_index=False)
        .agg(
            total_students=("student_id", "count"),
            placed_students=("placement_status", lambda s: (s == "Placed").sum()),
            avg_cgpa=("cgpa", "mean"),
            avg_package=("package_lpa", lambda s: s[s > 0].mean() if (s > 0).any() else 0),
            avg_risk_score=("placement_risk_score", "mean"),
        )
    )
    branch_summary["placement_rate"] = (branch_summary["placed_students"] / branch_summary["total_students"] * 100).round(2)

    company_summary = (
        df[df["placement_status"] == "Placed"]
        .groupby("company_name", as_index=False)
        .agg(
            hires=("student_id", "count"),
            avg_package=("package_lpa", "mean"),
            avg_cgpa=("cgpa", "mean"),
            avg_employability=("employability_score", "mean"),
        )
        .sort_values("hires", ascending=False)
    )

    yearly_summary = (
        df.groupby("placement_year", as_index=False)
        .agg(
            total_students=("student_id", "count"),
            placed_students=("placement_status", lambda s: (s == "Placed").sum()),
            avg_package=("package_lpa", lambda s: s[s > 0].mean() if (s > 0).any() else 0),
            avg_risk_score=("placement_risk_score", "mean"),
        )
        .sort_values("placement_year")
    )
    yearly_summary["placement_rate"] = (yearly_summary["placed_students"] / yearly_summary["total_students"] * 100).round(2)

    gender_summary = (
        df.groupby("gender", as_index=False)
        .agg(
            total_students=("student_id", "count"),
            placed_students=("placement_status", lambda s: (s == "Placed").sum()),
            avg_package=("package_lpa", lambda s: s[s > 0].mean() if (s > 0).any() else 0),
        )
    )
    gender_summary["placement_rate"] = (gender_summary["placed_students"] / gender_summary["total_students"] * 100).round(2)

    risk_summary = (
        df.groupby("risk_band", as_index=False)
        .agg(
            students=("student_id", "count"),
            avg_cgpa=("cgpa", "mean"),
            avg_risk=("placement_risk_score", "mean"),
        )
        .sort_values("avg_risk", ascending=False)
    )

    at_risk = df.sort_values(["placement_risk_score", "cgpa"], ascending=[False, True]).head(150)

    branch_summary.to_csv(MARTS_DIR / "branch_kpi_summary.csv", index=False)
    company_summary.to_csv(MARTS_DIR / "company_kpi_summary.csv", index=False)
    yearly_summary.to_csv(MARTS_DIR / "yearly_placement_trend.csv", index=False)
    gender_summary.to_csv(MARTS_DIR / "gender_placement_summary.csv", index=False)
    risk_summary.to_csv(MARTS_DIR / "risk_band_summary.csv", index=False)
    at_risk.to_csv(MARTS_DIR / "at_risk_students.csv", index=False)

    executive_kpis = {
        "total_students": int(df.shape[0]),
        "placed_students": int((df["placement_status"] == "Placed").sum()),
        "placement_rate": round(((df["placement_status"] == "Placed").mean()) * 100, 2),
        "average_package": round(float(df.loc[df["package_lpa"] > 0, "package_lpa"].mean()), 2),
        "highest_package": round(float(df["package_lpa"].max()), 2),
        "internship_conversion_rate": round((df["has_internship"].mean()) * 100, 2),
        "eligible_students": int(df["eligible_for_shortlist"].sum()),
        "at_risk_students": int((df["risk_band"] == "High").sum()),
    }

    with open(MARTS_DIR / "executive_kpis.json", "w", encoding="utf-8") as handle:
        json.dump(executive_kpis, handle, indent=2)


def save_sql_summaries(df: pd.DataFrame) -> None:
    """Create flat SQL-friendly extracts that mirror the dashboard questions."""
    sql_ready_dir = ROOT / "sql"
    sql_ready_dir.mkdir(parents=True, exist_ok=True)

    df[
        [
            "student_id",
            "gender",
            "age",
            "degree",
            "branch",
            "cgpa",
            "backlogs",
            "internships",
            "certifications",
            "coding_skills",
            "communication_skills",
            "project_count",
            "internship_status",
            "certification_status",
            "placement_status",
            "package_lpa",
            "company_name",
            "has_internship",
            "has_certification",
            "total_skill_score",
            "academic_performance_index",
            "employability_score",
            "placement_risk_score",
            "risk_band",
            "student_intervention",
            "placement_year",
        ]
    ].to_csv(sql_ready_dir / "placement_flat_table.csv", index=False)


def train_models(df: pd.DataFrame | None) -> None:
    """Train placement classification and salary regression models."""
    print("\n=== Step 4: Training and evaluating ML models ===")
    if df is None:
        return

    categorical_cols = ["gender", "degree", "branch"]
    numerical_cols = [
        "age",
        "cgpa",
        "backlogs",
        "internships",
        "certifications",
        "coding_skills",
        "communication_skills",
        "project_count",
        "has_internship",
        "has_certification",
        "total_skill_score",
        "academic_performance_index",
        "employability_score",
        "placement_risk_score",
        "eligible_for_shortlist",
    ]

    X = df[categorical_cols + numerical_cols]
    y_clf = (df["placement_status"] == "Placed").astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y_clf,
        test_size=0.2,
        random_state=42,
        stratify=y_clf,
    )

    preprocessor = ColumnTransformer(
        transformers=[("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)],
        remainder="passthrough",
    )

    models_to_test = {
        "Logistic Regression": LogisticRegression(max_iter=2000, random_state=42),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=150, random_state=42),
    }

    best_name = ""
    best_acc = -1.0
    best_pipeline: Pipeline | None = None

    for name, clf in models_to_test.items():
        pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("classifier", clf),
            ]
        )
        pipeline.fit(X_train, y_train)
        preds = pipeline.predict(X_test)
        acc = accuracy_score(y_test, preds)
        print(f"Model: {name} | Test Accuracy: {acc:.4f}")
        if acc > best_acc:
            best_acc = acc
            best_name = name
            best_pipeline = pipeline

    if best_pipeline is None:
        raise RuntimeError("No placement classification model could be trained.")

    print(f"Best placement model: {best_name} with accuracy {best_acc:.4f}")
    with open(MODELS_DIR / "placement_model.pkl", "wb") as handle:
        pickle.dump(best_pipeline, handle)

    df_placed = df[df["placement_status"] == "Placed"].copy()
    print(f"Training salary regressor on {len(df_placed)} placed students.")

    X_reg = df_placed[categorical_cols + numerical_cols]
    y_reg = df_placed["package_lpa"]
    X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
        X_reg,
        y_reg,
        test_size=0.2,
        random_state=42,
    )

    reg_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", LinearRegression()),
        ]
    )
    reg_pipeline.fit(X_train_r, y_train_r)
    train_pred = reg_pipeline.predict(X_train_r)
    test_pred = reg_pipeline.predict(X_test_r)
    train_r2 = r2_score(y_train_r, train_pred)
    test_r2 = r2_score(y_test_r, test_pred)
    print(f"Linear Regression R2 on Train: {train_r2:.4f}")
    print(f"Linear Regression R2 on Test: {test_r2:.4f}")

    with open(MODELS_DIR / "salary_model.pkl", "wb") as handle:
        pickle.dump(reg_pipeline, handle)

    model_metadata = {
        "best_classification_model": best_name,
        "classification_accuracy": round(best_acc, 4),
        "regression_train_r2": round(float(train_r2), 4),
        "regression_test_r2": round(float(test_r2), 4),
        "categorical_features": categorical_cols,
        "numerical_features": numerical_cols,
        "rows_used_for_training": int(df.shape[0]),
        "rows_used_for_salary_model": int(df_placed.shape[0]),
    }
    with open(MODELS_DIR / "model_metadata.json", "w", encoding="utf-8") as handle:
        json.dump(model_metadata, handle, indent=2)

    print("Saved model artifacts and metadata.")


def main() -> None:
    setup_project()
    enriched_df = enrich_data()
    cleaned_df = clean_and_process_data(enriched_df)
    train_models(cleaned_df)
    print("\n=== Project setup, ETL, and modeling complete ===")


if __name__ == "__main__":
    main()
