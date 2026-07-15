CREATE OR REPLACE VIEW Branch_Performance AS
SELECT
    b.Branch_Name,
    COUNT(*) AS Total_Students,
    SUM(p.Placement_Status = 'Placed') AS Placed_Students,
    ROUND(AVG(s.CGPA), 2) AS Avg_CGPA,
    ROUND(AVG(CASE WHEN p.Placement_Status = 'Placed' THEN p.Package_LPA END), 2) AS Avg_Package_LPA
FROM Students s
JOIN Branches b ON s.Branch_ID = b.Branch_ID
JOIN Placements p ON s.Student_ID = p.Student_ID
GROUP BY b.Branch_Name;

CREATE OR REPLACE VIEW Company_Recruitment_Summary AS
SELECT
    c.Company_Name,
    COUNT(*) AS Hires,
    ROUND(AVG(p.Package_LPA), 2) AS Avg_Package_LPA,
    ROUND(AVG(s.CGPA), 2) AS Avg_CGPA
FROM Placements p
JOIN Companies c ON p.Company_ID = c.Company_ID
JOIN Students s ON p.Student_ID = s.Student_ID
WHERE p.Placement_Status = 'Placed'
GROUP BY c.Company_Name;

CREATE OR REPLACE VIEW Gender_Placement_Summary AS
SELECT
    s.Gender,
    COUNT(*) AS Total_Students,
    SUM(p.Placement_Status = 'Placed') AS Placed_Students,
    ROUND(AVG(CASE WHEN p.Placement_Status = 'Placed' THEN p.Package_LPA END), 2) AS Avg_Package_LPA
FROM Students s
JOIN Placements p ON s.Student_ID = p.Student_ID
GROUP BY s.Gender;

CREATE OR REPLACE VIEW Risk_Intervention_View AS
SELECT
    r.student_id,
    r.branch,
    r.cgpa,
    r.backlogs,
    r.internships,
    r.coding_skills,
    r.communication_skills,
    r.placement_risk_score,
    r.risk_band,
    r.student_intervention
FROM placement_clean_raw r
WHERE r.risk_band IN ('Medium', 'High');
