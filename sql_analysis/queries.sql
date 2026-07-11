INSERT INTO
    Degrees(Degree_Name)
SELECT DISTINCT
    degree
FROM placement_clean_raw;

INSERT INTO
    Branches (Branch_Name)
SELECT DISTINCT
    branch
FROM placement_clean_raw;

INSERT INTO
    Companies (Company_Name)
SELECT DISTINCT
    company_name
FROM placement_clean_raw
WHERE
    company_name <> 'Unplaced';

INSERT INTO
    Students
SELECT r.student_id, r.gender, r.age, d.Degree_ID, b.Branch_ID, r.cgpa, r.backlogs, r.internships, r.certifications, r.coding_skills, r.communication_skills, r.project_count, r.total_skill_score, r.academic_performance_index, r.employability_score
FROM
    placement_clean_raw r
    JOIN Degrees d ON r.degree = d.Degree_Name
    JOIN Branches b ON r.branch = b.Branch_Name;

-- Placed students: link to their real company
INSERT INTO
    Placements (
        Student_ID,
        Company_ID,
        Package_LPA,
        Placement_Status
    )
SELECT r.student_id, c.Company_ID, r.package_lpa, r.placement_status
FROM
    placement_clean_raw r
    JOIN Companies c ON r.company_name = c.Company_Name
WHERE
    r.placement_status = 'Placed';

-- Not placed students: no company, NULL package
INSERT INTO
    Placements (
        Student_ID,
        Company_ID,
        Package_LPA,
        Placement_Status
    )
SELECT r.student_id, NULL, NULL, r.placement_status
FROM placement_clean_raw r
WHERE
    r.placement_status = 'Not Placed';