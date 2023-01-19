SELECT
	groups.name,
	AVG(grades.grade) as avg
FROM groups as groups
	INNER JOIN students as students ON groups.id = students.group_id
	INNER JOIN grades AS grades ON students.id = grades.student_id
WHERE grades.discipline_id = 3

GROUP BY
	groups.name

ORDER BY
	avg DESC