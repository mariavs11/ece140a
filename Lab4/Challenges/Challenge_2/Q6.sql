UPDATE Teachers
SET
    name = 'Ramsin'
WHERE
    name = 'Hoover';

SELECT Teachers.name,Courses.name
FROM Courses
INNER JOIN Teachers
ON Courses.teacher_id = Teachers.id ;


