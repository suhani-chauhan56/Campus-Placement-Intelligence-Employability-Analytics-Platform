SELECT *
FROM placement_clean_raw
WHERE
    cgpa IS NULL
    OR branch IS NULL;

DELETE p1
FROM
    placement_clean_raw p1
    JOIN placement_clean_raw p2 ON p1.student_id = p2.student_id
    AND p1.student_id > p2.student_id;

UPDATE placement_clean_raw
SET
    gender = TRIM(gender),
    degree = TRIM(degree),
    branch = TRIM(branch),
    company_name = TRIM(company_name);

SELECT * FROM placement_clean_raw WHERE cgpa NOT BETWEEN 0 AND 10;

SELECT * FROM placement_clean_raw WHERE backlogs < 0;

-- Data's already well-formed: Not Placed rows correctly show package_lpa = 0.0 and company_name = 'Unplaced'
SELECT placement_status, COUNT(*)
FROM placement_clean_raw
GROUP BY
    placement_status;