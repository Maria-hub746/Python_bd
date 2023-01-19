SELECT DISTINCT
    disciplines.name AS discipline

FROM grades AS grades
    LEFT JOIN disciplines AS disciplines ON grades.discipline_id = disciplines.id

WHERE grades.student_id = 1
    AND disciplines.teacher_id = 1

ORDER BY disciplines.name