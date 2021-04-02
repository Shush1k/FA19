-- Pract 6; Tasks: 8

/*
Задача 1 
Выбрать задачи длительностью более 100 дней, выполненные более чем 3 сотрудниками. 
*/
SELECT job_id FROM job_history  
WHERE end_date-start_date > 100  
GROUP BY job_id  
HAVING COUNT(*)>3 

/*
Задача 2 
Вывести подразделения и количество работников в нем, пронумеровать строки отчета, сортировать по алфавиту  
*/
SELECT department_name "Департамент", COUNT(*) "Кол-во сотрудников" FROM employees 
NATURAL JOIN departments  
GROUP BY department_name 

/*Задача 3 
Измените зарплату сотрудника 115 на 8000, если существующая зарплата меньше 6000. 
*/
UPDATE employees  
SET salary = 8000  
WHERE employee_id = 115 AND salary < 6000 

/*
Задача 4 
Удалите подразделение с ID 20 
*/
DELETE FROM departments  
WHERE department_id=20 

/*
Задача 5 
Измените идентификатор сотрудника задачи 110 на IT_PROG, если сотрудник принадлежит к отделу 10 и существующий идентификатор задания не начинается с IT. 
*/
UPDATE employees  
SET job_id= 'IT_PROG'  
WHERE employee_id=110 AND department_id=10 AND NOT job_id LIKE 'IT%' 

/*Задача 6 
Добавьте нового сотрудника со всеми необходимыми атрибутами. Произвольно. 
*/
INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, job_id)  
VALUES (125, 'Flynn', 'Taggart','FLYNN', SYSDATE, 'IT_PROG') 
 
/*Задача 7 
Создали новое подразделение и его руководителя, местоположение подразделения в Токио. Добавьте данные в БД.  
*/
-- Руководитель:
INSERT INTO employees (employee_id, manager_id, first_name, last_name, email, hire_date, job_id)  
VALUES (125, 125, 'Flynn', 'Taggart','FLYNN', SYSDATE, 'IT_PROG')  
-- Подразделение: 
INSERT INTO departments (department_id, department_name, manager_id) 
VALUES (111, 'Tokio', 125)  

/*Задача 8 
Создайте представление, отражающее подразделения, их местоположение, количество работников и руководителей. 
*/
SELECT manager_id, department_name, location_id, COUNT(*) "Cnt" 
FROM departments d 
JOIN employees e USING(manager_id) 
GROUP BY manager_id, department_name, location_id 