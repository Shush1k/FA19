-- Работает для MySQL
-- Упражнение 6-7
-- Баранов А. В. ПИ19-3

-- Задание 21
SELECT student_id, surname, stipend * 1.20 "stipend"
FROM student
ORDER BY stipend;

SELECT student_id, surname, stipend * 1.20 "stipend"
FROM student
ORDER BY surname;

-- Задание 22
SELECT student_id,
       MAX(mark) AS max_mark
FROM exam_marks
GROUP BY student_id;

SELECT student_id,
       MIN(mark) AS max_mark
FROM exam_marks
GROUP BY student_id;

-- Задание 23
SELECT semester, subj_name, subj_id
FROM subject
ORDER BY semester DESC;

SELECT semester, subj_name, subj_id
FROM subject
ORDER BY hour;

-- Задание 24
SELECT exam_date, SUM(mark) AS sum_mark
FROM exam_marks
GROUP BY exam_date
ORDER BY sum_mark DESC;

-- Задание 25
SELECT exam_date, TRUNCATE(AVG(mark), 1) AS avg_mark
FROM exam_marks
GROUP BY exam_date
ORDER BY avg_mark DESC;

SELECT exam_date, MIN(mark) AS avg_mark
FROM exam_marks
GROUP BY exam_date
ORDER BY avg_mark DESC;

SELECT exam_date, MAX(mark) AS avg_mark
FROM exam_marks
GROUP BY exam_date
ORDER BY avg_mark DESC;

-- Запросы с подзапросами
-- Задание 26
SELECT mark
FROM exam_marks
WHERE student_id = (
    SELECT student_id
    FROM student
    WHERE surname = "Сидоров"
);

-- Задание 27
SELECT name
FROM student
WHERE student_id IN (SELECT student_id
                     FROM exam_marks
                     WHERE subj_id = 101
                       AND mark > (SELECT AVG(mark) FROM exam_marks));

-- Задание 28
SELECT name
FROM student
WHERE student_id IN (SELECT student_id
                     FROM exam_marks
                     WHERE subj_id = 102
                       AND mark < (SELECT AVG(mark) FROM exam_marks));

-- Задание 29
SELECT student_id, COUNT(subj_id) AS cnt
FROM exam_marks
WHERE mark IS NOT NULL
GROUP BY student_id
HAVING cnt >= 20;

-- Задание 30
SELECT student_id, name, stipend
FROM student s1
WHERE s1.stipend = (SELECT MAX(s2.stipend)
                    FROM student s2
                    WHERE s1.city = s2.city);

-- Задание 31
SELECT name, student_id
FROM student
WHERE city NOT IN (SELECT DISTINCT city FROM university);

-- Задание 32
SELECT name, student_id
FROM student s
WHERE city NOT IN (SELECT city
                   FROM university
                   WHERE univ_id = s.univ_id);

SELECT s.name, s.student_id
FROM student s
         JOIN university u ON u.univ_id = s.univ_id
WHERE u.city != s.city;

-- Задание 33
SELECT *
FROM student s
WHERE EXISTS(
              SELECT *
              FROM university u
              WHERE rating > 300
                AND s.univ_id = u.univ_id
          );

-- Задание 34
SELECT s.*
FROM student s
         JOIN university u
WHERE u.rating > 300
  AND s.univ_id = u.univ_id;

-- Задание 35
SELECT *
FROM student s
WHERE EXISTS(SELECT * FROM university u WHERE s.city = u.city AND s.univ_id != u.univ_id);

-- Задание 36
SELECT subj_name
FROM subject s
WHERE EXISTS(SELECT mark FROM exam_marks e WHERE mark IS NOT NULL AND s.subj_id = e.subj_id);