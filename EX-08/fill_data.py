import random
from datetime import datetime
import faker
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_DISCIPLINES = 5
#DISCIPLINES = 'Algebra', 'Biology', 'Drawing', 'Chemisty', 'Geography', 'Geometry', 'History', 'Literature', 'Mathematics', 'Music', 'Physical education', 'Physics', 'Technology'
NUMBER_TEACHERS = 3
NUMBER_GRADES = 20


def generate_fake_data(number_groups, number_students, number_disciplines, number_teachers, number_grades) -> tuple():
    fake_groups = []  # здесь будем хранить компании
    fake_students = []  # здесь будем хранить сотрудников
    fake_disciplines = []  # здесь будем хранить предметы
    fake_teachers = []  # здесь будем хранить учителей
    fake_grades = []  # здесь будем хранить оценки
    '''Возьмём три групы из faker и поместим их в нужную переменную'''
    fake_data = faker.Faker()

    # Создадим набор компаний в количестве number_companies
    for _ in range(number_groups):
        fake_groups.append(fake_data.company())

    # Сгенерируем теперь number_employees количество сотрудников'''
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # И number_post набор должностей
    for _ in range(number_disciplines):
        fake_disciplines.append(fake_data.job())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for grade in range(number_grades):
        fake_grades.append((random.randint(1, number_students), random.randint(1, number_disciplines), grade,
                           fake_data.date_between_dates(datetime(2022, 1, 1), datetime(2022, 12, 31))))

#date_time;
    return fake_groups, fake_students, fake_disciplines, fake_teachers, fake_grades


def prepare_data(groups, students, disciplines, teachers, grades) -> tuple():
    for_groups = []
    for group in groups:
        for_groups.append((group, ))

    for_students = []  # для таблицы employees
    for student in students:
        for_students.append((student, random.randint(1, NUMBER_GROUPS)))

    for_disciplines = []  # для таблицы employees
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
    # Создадим соединение с нашей БД и получим объект курсора для манипуляций с данными

    with sqlite3.connect('salary.db') as con:

        cur = con.cursor()

        '''Заполняем таблицу компаний. И создаем скрипт для вставки, где переменные, которые будем вставлять отметим
        знаком заполнителя (?) '''

        sql_to_groups = """INSERT INTO [groups](name)
                               VALUES (?)"""

        '''Для вставки сразу всех данных воспользуемся методом executemany курсора. Первым параметром будет текст
        скрипта, а вторым данные (список кортежей).'''

        cur.executemany(sql_to_groups, groups)

        # Далее вставляем данные о сотрудниках. Напишем для него скрипт и укажем переменные

        sql_to_students = """INSERT INTO students(fullname, group_id)
                               VALUES (?, ?)"""

        # Данные были подготовлены заранее, потому просто передаем их в функцию

        cur.executemany(sql_to_students, students)

        sql_to_disciplines = """INSERT INTO disciplines(name, teacher_id)
                                       VALUES (?, ?)"""

        # Данные были подготовлены заранее, потому просто передаем их в функцию

        cur.executemany(sql_to_disciplines, disciplines)

        sql_to_teachers = """INSERT INTO teachers(fullname)
                                               VALUES (?)"""

        # Данные были подготовлены заранее, потому просто передаем их в функцию

        cur.executemany(sql_to_teachers, teachers)

        # Последней заполняем таблицу с зарплатами
        sql_to_grades = """INSERT INTO grades(student_id, discipline_id, grade, date_of)
                              VALUES (?, ?, ?, ?)"""

        # Вставляем данные о зарплатах

        cur.executemany(sql_to_grades, grades)

        # Фиксируем наши изменения в БД

        con.commit()

if __name__ == '__main__':
    groups, students, disciplines, teachers, grades = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_DISCIPLINES, NUMBER_TEACHERS, NUMBER_GRADES))
    insert_data_to_db(groups, students, disciplines, teachers, grades)
    print(grades)
