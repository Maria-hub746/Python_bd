-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(255) NOT NULL,
    group_id REFERENCES [groups] (id)
);

-- Table: [groups]
DROP TABLE IF EXISTS [groups];
CREATE TABLE [groups] (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(255) NOT NULL
);

-- Table: disciplines
DROP TABLE IF EXISTS disciplines;
CREATE TABLE disciplines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    teacher_id REFERENCES teachers (id)
);

-- Table: disciplines
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id REFERENCES students (id),
    discipline_id REFERENCES disciplines (id),
    grade INTEGER NOT NULL,
    date_of DATE NOT NULL
);