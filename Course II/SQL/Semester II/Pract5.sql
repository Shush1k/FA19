
/*
Задача 1 
Отделу кадров требуется запрос, при запуске которого пользователь вводит фамилию сотрудника. Далее, в качестве результата отображается фамилия и дата приёма на работу всех сотрудников из того же отдела, что и заданный пользователем сотрудник (исключая этого сотрудника).  Например, если пользователь введет Zlotkey, будут найдены все сотрудники, которые работают с Zlotkey (исключая Zlotkey). 
*/
SELECT emp.last_name, emp.hire_date  
FROM employees emp 
WHERE emp.department_id IN (SELECT department_id FROM employees WHERE last_name=:f) AND last_name!=:f; 
 
/*
Задача 2 
Создайте отчёт, который отображает номер сотрудника, фамилию и зарплату для всех сотрудников, которые зарабатывают больше, чем средняя зарплата. Сортируйте результат в порядке возрастания зарплаты.  
*/
SELECT emp.employee_id, emp.last_name, emp.salary 
FROM employees emp 
WHERE emp.salary > (SELECT AVG(salary) FROM employees) 
ORDER BY emp.salary; 

/*
Задача 3 
Напишите запрос, который отображает номер сотрудника и фамилию для всех сотрудников, которые работают в отделе с любым сотрудником, фамилия которого содержит букву u. 
Замешательство: Должна ли буква 'u' быть заглавной? (Начало имени) 
*/
SELECT emp.employee_id, emp.last_name 
FROM employees emp WHERE emp.department_id IN  
(SELECT department_id FROM employees WHERE last_name LIKE '%u%'); 

/*
Задача 4 
Отделу кадров необходим отчёт, который отображает фамилию, номер отдела и должность для всех сотрудников, расположение отдела которых 1700. 
*/
SELECT emp.last_name, emp.department_id, emp.job_id 
FROM employees emp 
WHERE emp.department_id IN (SELECT department_id FROM departments 
WHERE location_id = 1700);  

/*
Задача 4.1 
Отделу кадров необходим отчёт, который отображает фамилию, номер отдела и должность для всех сотрудников, расположение отдела которых 1700. 
Измените запрос таким образом, чтобы пользователь мог вызвать расположение отдела. 
*/
SELECT emp.last_name, emp.department_id, emp.job_id 
FROM employees emp 
WHERE emp.department_id IN (SELECT department_id FROM departments 
WHERE location_id = :f); 

/*
Задача 5 
Создайте отчёт для отдела кадров, который отображает фамилию и зарплату всех сотрудников, которые работают с King. 
*/
SELECT emp.last_name, emp.salary 
FROM employees emp 
WHERE emp.manager_id IN  
(SELECT employee_id FROM employees WHERE last_name = 'King'); 

/*
Задача 6 
Создайте отчёт для отдела кадров, который отображает номер отдела, фамилию и должность для всех сотрудников в отделе  Executive. 
*/
SELECT emp.department_id, emp.last_name, emp.job_id 
FROM employees emp 
WHERE emp.department_id IN  
(SELECT department_id FROM departments WHERE department_name = 'Executive'); 

/*
Задача 7 
Измените запрос "Задача 3", чтобы отобразить номер сотрудника, фамилию и зарплату для всех сотрудников, которые зарабатывают больше, чем средняя зарплата, и которые работают в отделе с любым сотрудником, фамилия которого содержит букву  u. 
ВНИМАНИЕ. Результат должен включать сотрудников, фамилия которых содержит букву u. 
*/
SELECT emp.employee_id, emp.last_name, emp.salary 
FROM employees emp  
WHERE emp.department_id IN  (SELECT department_id FROM employees WHERE last_name LIKE '%u%') 
AND emp.salary > (SELECT AVG(salary) FROM employees);