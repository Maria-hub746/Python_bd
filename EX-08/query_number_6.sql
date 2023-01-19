SELECT
    students.fullname AS fullname

FROM
    students AS students

WHERE students.group_id = :group_id