SELECT
    students.fullname AS fullname,
    disciplines.name AS discipline

FROM students AS students
    INNER JOIN grades AS grades ON students.id = grades.student_id
    INNER JOIN disciplines AS disciplines ON grades.discipline_id = disciplines.id

ORDER BY students.fullname