
CREATE TABLE Teachers(
id int,
name VARCHAR(15) NOT NULL
);

CREATE TABLE Students(
id int,
name VARCHAR(15) NOT NULL,
email VARCHAR(40) NOT NULL,
password VARCHAR(9) NOT NULL
);
CREATE TABLE Grades(
student_id int,
course_id int,
grade VARCHAR(2) NOT NULL
);
CREATE TABLE Courses(
id integer,
name VARCHAR(30) NOT NULL,
teacher_id int
);