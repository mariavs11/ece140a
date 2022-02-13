SELECT Grades.student_id, Students.name, Grades.course_id, Grades.grade
FROM Grades
INNER JOIN Students
ON Grades.student_id = Students.id;

