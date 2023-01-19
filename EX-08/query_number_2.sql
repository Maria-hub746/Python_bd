SELECT
	students.fullname AS fullname,
	AVG(grades.grade) AS avg
FROM
	students AS students
		INNER JOIN grades AS grades
		ON students.id = grades.student_id

WHERE grades.discipline_id = :discipline_id

GROUP BY
	students.fullname

ORDER BY
	avg DESC

LIMIT 1