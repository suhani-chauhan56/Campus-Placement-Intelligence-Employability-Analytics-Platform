-- Executive KPIs
SELECT
    COUNT(*) AS total_students,
    SUM(placement_status = 'Placed') AS placed_students,
    ROUND(AVG(CASE WHEN placement_status = 'Placed' THEN package_lpa END), 2) AS avg_package_lpa,
    ROUND(MAX(package_lpa), 2) AS highest_package_lpa,
    ROUND(AVG(has_internship) * 100, 2) AS internship_conversion_rate,
    SUM(eligible_for_shortlist) AS eligible_students,
    SUM(risk_band = 'High') AS at_risk_students
FROM placement_clean_raw;

-- Top 10 companies hiring students
SELECT
    company_name,
    COUNT(*) AS hires,
    ROUND(AVG(package_lpa), 2) AS avg_package_lpa
FROM placement_clean_raw
WHERE placement_status = 'Placed'
GROUP BY company_name
ORDER BY hires DESC, avg_package_lpa DESC
LIMIT 10;

-- Branch with the highest package
SELECT
    branch,
    ROUND(MAX(package_lpa), 2) AS highest_package_lpa
FROM placement_clean_raw
WHERE placement_status = 'Placed'
GROUP BY branch
ORDER BY highest_package_lpa DESC
LIMIT 1;

-- Average CGPA by company
SELECT
    company_name,
    ROUND(AVG(cgpa), 2) AS avg_cgpa,
    COUNT(*) AS hires
FROM placement_clean_raw
WHERE placement_status = 'Placed'
GROUP BY company_name
ORDER BY avg_cgpa DESC;

-- Students with internship but no placement
SELECT *
FROM placement_clean_raw
WHERE internship_status = 'Yes'
  AND placement_status = 'Not Placed'
ORDER BY placement_risk_score DESC;

-- Placement rate by gender
SELECT
    gender,
    COUNT(*) AS total_students,
    SUM(placement_status = 'Placed') AS placed_students,
    ROUND(SUM(placement_status = 'Placed') / COUNT(*) * 100, 2) AS placement_rate_pct
FROM placement_clean_raw
GROUP BY gender;

-- Package distribution buckets
SELECT
    CASE
        WHEN package_lpa = 0 THEN 'Not Placed'
        WHEN package_lpa < 6 THEN '3-6 LPA'
        WHEN package_lpa < 9 THEN '6-9 LPA'
        WHEN package_lpa < 12 THEN '9-12 LPA'
        ELSE '12+ LPA'
    END AS package_band,
    COUNT(*) AS students
FROM placement_clean_raw
GROUP BY package_band
ORDER BY students DESC;

-- Students requiring intervention
SELECT
    student_id,
    branch,
    cgpa,
    backlogs,
    internships,
    coding_skills,
    communication_skills,
    placement_risk_score,
    student_intervention
FROM placement_clean_raw
WHERE risk_band = 'High'
ORDER BY placement_risk_score DESC
LIMIT 100;
