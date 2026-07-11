CREATE OR REPLACE VIEW Branch_Performance AS
SELECT b.Branch_Name, COUNT(*) AS Total, SUM(p.Placement_Status = 'Placed') AS Placed
FROM
    Students s
    JOIN Branches b ON s.Branch_ID = b.Branch_ID
    JOIN Placements p ON s.Student_ID = p.Student_ID
GROUP BY
    b.Branch_Name;

CREATE OR REPLACE VIEW Salary_Insights AS
SELECT s.Student_ID, b.Branch_Name, p.Package_LPA
FROM
    Students s
    JOIN Branches b ON s.Branch_ID = b.Branch_ID
    JOIN Placements p ON s.Student_ID = p.Student_ID
WHERE
    p.Placement_Status = 'Placed';