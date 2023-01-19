import random
from datetime import datetime
import faker
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_DISCIPLINES = 5
NUMBER_TEACHERS = 3
NUMBER_GRADES = 20


def generate_fake_data(number_groups, number_students, number_disciplines, number_teachers, number_grades) -> tuple():
    fake_groups = []
    fake_students = []
    fake_disciplines = []
    fake_teachers = []
    fake_grades = []
    '''Возьмём три групы из faker и поместим их в нужную переменную'''
    fake_data = faker.Faker()


    for _ in range(number_groups):
        fake_groups.append(fake_data.company())


    for _ in range(number_students):
        fake_students.append(fake_data.name())


    for _ in range(number_disciplines):
        fake_disciplines.append(fake_data.job())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())




    return fake_groups, fake_students, fake_disciplines, fake_teachers, fake_grades


def prepare_data(groups, students, disciplines, teachers, grades) -> tuple():
    for_groups = []
    for group in groups:
        for_groups.append((group, ))

    for_students = []
    for student in students:
        for_students.append((student, random.randint(1, NUMBER_GROUPS)))

    for_disciplines = []
    for discipline in disciplines:
        for_disciplines.append((discipline, random.randint(1, NUMBER_TEACHERS)))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_grades = []

    for month in range(1, 12 + 1):
        student_date = datetime(2021, month, random.randint(10, 20)).date()
        for student in range(1, NUMBER_STUDENTS + 1):
            for_grades.append((student, random.randint(1, NUMBER_DISCIPLINES), random.randint(1, 12), student_date))

    return for_groups, for_students, for_disciplines, for_teachers, for_grades


def insert_data_to_db(groups, students, disciplines, teachers, grades) -> None:

    with sqlite3.connect('salary.db') as con:

        cur = con.cursor()


        sql_to_groups = """INSERT INTO [groups](name)
                               VALUES (?)"""


        cur.executemany(sql_to_groups, groups)



        sql_to_students = """INSERT INTO students(fullname, group_id)
                               VALUES (?, ?)"""


        cur.executemany(sql_to_students, students)

        sql_to_disciplines = """INSERT INTO disciplines(name, teacher_id)
                                       VALUES (?, ?)"""



        cur.executemany(sql_to_disciplines, disciplines)

        sql_to_teachers = """INSERT INTO teachers(fullname)
                                               VALUES (?)"""



        cur.executemany(sql_to_teachers, teachers)


        sql_to_grades = """INSERT INTO grades(student_id, discipline_id, grade, date_of)
                              VALUES (?, ?, ?, ?)"""



        cur.executemany(sql_to_grades, grades)


        con.commit()

if __name__ == '__main__':
    groups, students, disciplines, teachers, grades = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_DISCIPLINES, NUMBER_TEACHERS, NUMBER_GRADES))
    insert_data_to_db(groups, students, disciplines, teachers, grades)
    print(grades)
