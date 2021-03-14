-- Для MySQL
-- Баранов А. В. ПИ19-3

-- Задание 1
SELECT CONCAT(student_id ,';', UPPER(surname),';',UPPER(name),';',stipend,';', kurs,';', 
UPPER(city),';',DATE_FORMAT(birthday, '%Y/%m/%d'),';',univ_id)
AS "Total" FROM student;

-- Задание 2
SELECT CONCAT(SUBSTR(name, 1, 1), '.', surname,'; место жительства-', UPPER(city),'; родился - ',
DATE_FORMAT(birthday, '%d.%m.%Y')) AS "Total" FROM  student;

-- Задание 3
SELECT CONCAT(LOWER(CONCAT(SUBSTR(name, 1, 1), '.', surname)), '; место жительства-', LOWER(city), '; родился - ', 
DATE_FORMAT(birthday, '%d-%M-%Y'))  AS  "Total"  FROM  student;

-- Задание 4
SELECT CONCAT(name,' ', surname, ' родился в ', DATE_FORMAT(birthday, '%Y'), ' году')
FROM student;

-- Задание 5
SELECT name, surname, stipend * 100 AS "x100 stipend" FROM student;

-- Задание 6
SELECT CONCAT(UPPER(CONCAT(name, ' ', surname)), ' родился в ', DATE_FORMAT(birthday, '%Y'), ' году') AS  result
FROM student
WHERE kurs IN (1,2,4);

-- Задание 7
SELECT CONCAT('Код-', univ_id, '; ', univ_name, '-г.', UPPER(city ), '; Рейтинг=', rating)  AS result FROM university;

-- Задание 8
SELECT CONCAT('Код-', univ_id, '; ', univ_name, '-г.', UPPER(city ), '; Рейтинг=', ROUND(rating, -2))  AS result FROM university;

-- Задание 9
SELECT COUNT(student_id) AS "Count"
FROM exam_marks
WHERE subj_id=20;

-- Задание 10
SELECT COUNT(DISTINCT(subj_id))
FROM exam_marks;

-- Задание 11
SELECT student_id, MIN(mark)
FROM exam_marks
GROUP BY student_id;

-- Задание 12
SELECT student_id, MAX(mark) FROM exam_marks
GROUP BY student_id;

-- Задание 13
SELECT surname FROM student 
WHERE surname LIKE "И%" LIMIT 1;

-- Задание 14
SELECT subj_id, MAX(semester) "Max_semester" FROM subject
GROUP BY subj_id;

-- Задание 15
SELECT COUNT(DISTINCT student_id) "Кол-во студентов", exam_date , exam_id  
FROM exam_marks
GROUP BY exam_id;

-- Задание 16
SELECT s.kurs, TRUNCATE(AVG(e.mark), 1) "Ср. оценка", e.subj_id
FROM student s
JOIN exam_marks e ON s.student_id = e.student_id
GROUP BY s.kurs, e.subj_id;

-- Задание 17
SELECT student_id, TRUNCATE(AVG(mark), 1) "Ср. оценка"
FROM exam_marks
GROUP BY student_id;

-- Задание 18
SELECT exam_id, TRUNCATE(AVG(mark), 1) "Ср. оценка"
FROM exam_marks
GROUP BY exam_id;

-- Задание 19
SELECT exam_id, COUNT(student_id) "Кол-во студентов"
FROM exam_marks
GROUP BY exam_id;

-- Задание 20
-- база данных некорректная нельзя связать таблицу subject по полю курс
-- в примере ниже видно почему
SELECT st.kurs, count(s.subj_id) as  "Кол-во предметов'"
FROM subject s
JOIN exam_marks e ON s.subj_id = e.subj_id
JOIN student st ON e.student_id = st.student_id
GROUP BY st.kurs;