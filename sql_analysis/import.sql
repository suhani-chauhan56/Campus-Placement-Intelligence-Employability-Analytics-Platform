LOAD DATA LOCAL INFILE 'C:\\Users\\HP\\Desktop\\placement project\\data\\cleaned\\placement_data_cleaned.csv' INTO
TABLE placement_clean_raw FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS (
    student_id,
    gender,
    age,
    degree,
    branch,
    cgpa,
    backlogs,
    internships,
    certifications,
    coding_skills,
    communication_skills,
    project_count,
    internship_status,
    certification_status,
    placement_status,
    package_lpa,
    company_name,
    has_internship,
    has_certification,
    total_skill_score,
    academic_performance_index,
    employability_score
);

SELECT COUNT(*) FROM placement_clean_raw;
-- expect 12000