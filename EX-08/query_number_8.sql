SELECT
    teachers.fullname AS fullname,
    AVG(grades.grade) AS avg

FROM teachers AS teachers
    LEFT JOIN disciplines AS disciplines ON teachers.id = disciplines.teacher_id
        LEFT JOIN grades AS grades ON disciplines.id = grades.discipline_id

WHERE
    teachers.id = :teachers.id
GROUP BY
    teachers.fullname