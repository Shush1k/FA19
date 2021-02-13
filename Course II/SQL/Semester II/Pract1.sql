/*
Задача 1 
Из-за проблем с бюджетом отделу кадров необходим отчёт, в котором отображены фамилия и зарплата сотрудников, зарабатывающих больше $12,000.  
*/
SELECT last_name, salary 
FROM employees 
WHERE salary > 12000;  

/*
Задача 2 
Создайте отчёт, который отображает фамилию и номер отдела для сотрудника с номером 176. 
*/
SELECT last_name, department_id 
FROM employees 
WHERE employee_id = 176;

/*
Задача 3 
Отделу кадров нужно найти самых высокооплачиваемых и низкооплачиваемых сотрудников. 
Измените так, чтобы показать фамилию и зарплату для любого сотрудника, зарплата которого не попадает в диапазон от $5,000 до  $12,000. 
*/
SELECT last_name, salary 
FROM employees 
ORDER BY salary DESC; 

SELECT last_name, salary 
FROM employees 
WHERE salary > 12000 OR salary < 5000; 

/*
Задача 4 
Создайте отчёт, который показывает фамилию, должность и дату приема на работу сотрудников с фамилиями Matos и Taylor.
Отсортируйте данные в порядке возрастания дат приема на работу.  
*/
SELECT last_name, job_id, hire_date 
FROM employees 
WHERE last_name = 'Taylor' 
OR last_name = 'Matos' 
ORDER BY hire_date; 

/*
Задача 5 
Отобразите фамилию и номер отдела всех сотрудников из отделов 20 или 50 и отсортируйте по имени в алфавитном порядке. 
*/
SELECT first_name, last_name, department_id 
FROM employees 
WHERE department_id = 20 
OR department_id = 50 
ORDER BY first_name; 

/*
Задача 6
Измените запрос задания 3 так, чтобы показать фамилию и зарплату сотрудников, которые зарабатывают от $5,000 до $12,000 и числятся в отделах  20 или 50.  
Озаглавьте поля Employee and Monthly Salary, соответственно. 
*/
SELECT last_name AS "Employee" , salary AS "Monthly Salary" 
FROM employees  
WHERE salary > 5000  
AND salary < 12000 
AND department_id = 50  
OR department_id = 20;

/*
Задача 7 
Отдел кадров нуждается в отчёте, который показывает фамилию и дату найма всех сотрудников, принятых в 1994 г.  
*/
SELECT last_name, hire_date 
FROM employees 
WHERE hire_date LIKE '1994%'; 

/*
Задача 8 
Создайте отчёт, который показывает фамилию и код должности всех сотрудников, у которых нет начальника.  
*/
SELECT last_name, job_id 
FROM employees 
WHERE manager_id IS NULL; 

/*
Задача 9 
Создайте отчёт, который отображает фамилию, зарплату и % комиссионных всех сотрудников, которые получают комиссионные. Отсортируйте данные в порядке убывания зарплаты и % комиссионных. 
*/
SELECT last_name, salary, commission_pct 
FROM employees 
WHERE commission_pct IS NOT NULL 
ORDER BY salary DESC; 
 
SELECT last_name, salary, commission_pct 
FROM employees 
WHERE commission_pct IS NOT NULL 
ORDER BY commission_pct DESC; 


/*
Задача 12 
Отобразите фамилии всех сотрудников, у которых третья буква - a. 
*/
SELECT last_name 
FROM employees 
WHERE last_name LIKE '__a%'; 

/*
Задача 13 
Отобразите фамилии всех сотрудников, у которых есть и a, и e в их фамилии. 
*/
SELECT last_name 
FROM employees 
WHERE last_name LIKE '%a%' and last_name LIKE '%e%'; 

/*
Задача 14 
Отобразите фамилию, должность и зарплату всех сотрудников, у которых должность SA_REP или ST_CLERK и зарплата которых не равна $2,500, $3,500 или  $7,000. 
*/
SELECT last_name, job_id, salary 
FROM employees 
WHERE (job_id = 'SA_REP' OR job_id = 'ST_CLERK') 
AND salary NOT IN (2500, 3500, 7000);

/*
Задача 15 
Отобразить фамилию, зарплату, и % комиссионных всех сотрудников, у которых комиссионные – 20%. 
*/
SELECT last_name, salary, commission_pct 
FROM employees 
WHERE commission_pct = .2; 
