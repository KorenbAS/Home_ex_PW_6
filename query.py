-- query_1.sql
SELECT students.student_id, students.name, AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.student_id = grades.student_id
GROUP BY students.student_id
ORDER BY average_grade DESC
LIMIT 5;

-- query_2.sql
SELECT s.student_id, s.name, AVG(g.grade) as average_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
WHERE g.subject_id = 1  -- Замініть 1 на ідентифікатор конкретного предмета
GROUP BY s.student_id, s.name
ORDER BY average_grade DESC
LIMIT 1;

-- query_3.sql
SELECT g.subject_id, s.group_id, AVG(g.grade) as average_grade
FROM grades g
JOIN students s ON g.student_id = s.student_id
WHERE g.subject_id = 1  -- Замініть 1 на ідентифікатор конкретного предмета
GROUP BY g.subject_id, s.group_id
ORDER BY s.group_id, average_grade DESC;

-- query_4.sql
SELECT AVG(grade) as average_grade
FROM grades;

-- query_5.sql
SELECT subject_name
FROM subjects
WHERE teacher_id = 1;  -- Замініть 1 на ідентифікатор конкретного викладача

-- query_6.sql
SELECT *
FROM students
WHERE group_id = 1;  -- Замініть 1 на ідентифікатор конкретної групи

-- query_7.sql
SELECT s.name as student_name, g.grade, g.date_received
FROM grades g
JOIN students s ON g.student_id = s.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE s.group_id = 1 AND sub.subject_id = 2;  -- Замініть 1 і 2 на ідентифікатори конкретної групи та предмета

-- query_8.sql
SELECT AVG(g.grade) as average_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE sub.teacher_id = 1;  -- Замініть 1 на ідентифікатор конкретного викладача

-- query_9.sql
SELECT DISTINCT sub.subject_name
FROM subjects sub
JOIN grades g ON sub.subject_id = g.subject_id
JOIN students s ON g.student_id = s.student_id
WHERE s.student_id = 1;  -- Замініть 1 на ідентифікатор конкретного студента

-- query_10.sql
SELECT DISTINCT sub.subject_name
FROM subjects sub
JOIN grades g ON sub.subject_id = g.subject_id
JOIN students s ON g.student_id = s.student_id
JOIN teachers t ON sub.teacher_id = t.teacher_id
WHERE s.student_id = 1 AND t.teacher_id = 2;  -- Замініть 1 та 2 на ідентифікатори конкретного студента та викладача

# _________________________________________________________________________________________________________
# Додаткове завдання

-- query_11.sql
SELECT AVG(g.grade) as average_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.subject_id
JOIN students s ON g.student_id = s.student_id
WHERE sub.teacher_id = 1 AND s.student_id = 2;  -- Замініть 1 та 2 на ідентифікатори конкретного викладача та студента

-- query_12.sql
SELECT s.name as student_name, g.grade, g.date_received
FROM grades g
JOIN students s ON g.student_id = s.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE s.group_id = 1 AND sub.subject_id = 2
ORDER BY g.date_received DESC
LIMIT 1;
