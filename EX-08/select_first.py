import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT DISTINCT
    disciplines.name AS discipline

FROM grades AS grades
    LEFT JOIN disciplines AS disciplines ON grades.discipline_id = disciplines.id

WHERE grades.student_id = 1
    AND disciplines.teacher_id = 1

ORDER BY disciplines.name
"""
if __name__ == '__main__':

    print(execute_query(sql))

