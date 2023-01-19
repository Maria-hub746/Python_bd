SELECT
    teachers.fullname AS fullname,
    disciplines.name AS discipline
FROM
    teachers AS teachers
    LEFT JOIN disciplines AS disciplines ON teachers.id = disciplines.teacher_id

WHERE
    teachers.id = :teachers_id