CREATE DATABASE IF NOT EXISTS Placement_Analytics;

USE Placement_Analytics;

DROP TABLE IF EXISTS placement_clean_raw;

CREATE TABLE placement_clean_raw (
    student_id INT,
    gender VARCHAR(10),
    age INT,
    degree VARCHAR(20),
    branch VARCHAR(50),
    cgpa DECIMAL(4, 2),
    backlogs INT,
    internships INT,
    certifications INT,
    coding_skills INT,
    communication_skills INT,
    project_count INT,
    internship_status VARCHAR(5),
    certification_status VARCHAR(5),
    placement_status VARCHAR(20),
    package_lpa DECIMAL(5, 2),
    company_name VARCHAR(50),
    has_internship TINYINT,
    has_certification TINYINT,
    total_skill_score INT,
    academic_performance_index DECIMAL(5, 2),
    employability_score DECIMAL(6, 2)
);

DROP TABLE IF EXISTS Degrees;

CREATE TABLE Degrees(
    Degree_ID INT AUTO_INCREMENT PRIMARY KEY,
    Degree_Name VARCHAR(20) UNIQUE
);

DROP TABLE IF EXISTS Branches;

CREATE TABLE Branches (
    Branch_ID INT AUTO_INCREMENT PRIMARY KEY,
    Branch_Name VARCHAR(50) UNIQUE
);

DROP TABLE IF EXISTS Companies;

CREATE TABLE Companies (
    Company_ID INT AUTO_INCREMENT PRIMARY KEY,
    Company_Name VARCHAR(50) UNIQUE
);

DROP TABLE IF EXISTS Students;

CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Gender VARCHAR(10),
    Age INT,
    Degree_ID INT,
    Branch_ID INT,
    CGPA DECIMAL(4, 2) CHECK (CGPA BETWEEN 0 AND 10),
    Backlogs INT DEFAULT 0,
    Internships INT DEFAULT 0,
    Certifications INT DEFAULT 0,
    Coding_Skills INT DEFAULT 0,
    Communication_Skills INT DEFAULT 0,
    Project_Count INT DEFAULT 0,
    Total_Skill_Score INT,
    Academic_Performance_Index DECIMAL(5, 2),
    Employability_Score DECIMAL(6, 2),
    FOREIGN KEY (Degree_ID) REFERENCES Degrees(Degree_ID),
    FOREIGN KEY (Branch_ID) REFERENCES Branches (Branch_ID)
);

DROP TABLE IF EXISTS Placements;

CREATE TABLE Placements (
    Placement_ID INT AUTO_INCREMENT PRIMARY KEY,
    Student_ID INT,
    Company_ID INT NULL,
    Package_LPA DECIMAL(5, 2),
    Placement_Status VARCHAR(20) NOT NULL,
    FOREIGN KEY (Student_ID) REFERENCES Students (Student_ID),
    FOREIGN KEY (Company_ID) REFERENCES Companies (Company_ID)
);