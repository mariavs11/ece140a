LOAD DATA INFILE '/usr/local/mysql-8.0.28-macos11-x86_64/uploads/students.csv'
INTO TABLE Students
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/usr/local/mysql-8.0.28-macos11-x86_64/uploads/courses.csv'
INTO TABLE Courses
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/usr/local/mysql-8.0.28-macos11-x86_64/uploads/grades.csv'
INTO TABLE Grades
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/usr/local/mysql-8.0.28-macos11-x86_64/uploads/teachers.csv'
INTO TABLE Teachers
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;