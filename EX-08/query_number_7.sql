SELECT
    students.fullname AS fullname,
    grades.grade AS grade

FROM students AS students
    INNER JOIN grades AS grades ON students.id = grades.student_id

WHERE students.group_id = :group_id
    AND grades.discipline_id = :discipline_i