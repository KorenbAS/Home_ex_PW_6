import logging

from faker import Faker
import sqlite3
from sqlite3 import DatabaseError
import random

conn = sqlite3.connect('./SQLiteDB.sqlite')
cursor = conn.cursor()

# Ініціалізація Faker
fake = Faker('uk-Ua')

# Створення таблиці студентів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(group_id)
    )
''')

# Створення таблиці груп
cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        group_id INTEGER PRIMARY KEY,
        group_name TEXT
    )
''')

# Створення таблиці викладачів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

# Створення таблиці предметів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INTEGER PRIMARY KEY,
        subject_name TEXT,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
    )
''')

# Створення таблиці оцінок
cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        grade_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date_received DATE,
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
    )
''')

# Функція для отримання випадкового ідентифікатора вчителя
def get_random_teacher_id():
    return random.randint(1, 5)  # Припустимо, що у нас 5 вчителів

# Додавання груп
groups = [('Group A',), ('Group B',), ('Group C',)]
cursor.executemany('INSERT INTO groups (group_name) VALUES (?)', groups)

# Додавання вчителів
teachers = [(fake.name(),) for _ in range(5)]
cursor.executemany('INSERT INTO teachers (name) VALUES (?)', teachers)

# Додавання предметів
subjects = [(fake.word(), get_random_teacher_id()) for _ in range(8)]
cursor.executemany('INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)', subjects)

# Додавання студентів
students = [(fake.name(), random.randint(1, 3)) for _ in range(50)]  # Припустимо, що у нас 3 групи
cursor.executemany('INSERT INTO students (name, group_id) VALUES (?, ?)', students)

# Додавання оцінок
for student_id in range(1, 51):
    for subject_id in range(1, 9):
        grades = [(student_id, subject_id, random.randint(60, 100), fake.date_between(start_date='-30d', end_date='today')) for _ in range(20)]
        cursor.executemany('INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)', grades)


# Збереження змін та закриття з'єднання
try:
    # Збереження змін
    conn.commit()
except DatabaseError as e:
    logging.error(e)
    conn.rollback()
finally:
    # Закриття підключення
    cursor.close()
    conn.close()