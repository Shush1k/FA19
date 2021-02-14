/*
Задача 1 
Создайте запрос для отдела кадров, чтобы отобразить адреса всех отделов. Используйте таблицы locations и countries. 
Покажите территориальное расположение,  улицу, город, государство или область, и страну на выходе. Используйте NATURAL JOIN , чтобы отобразить результат.  
*/
SELECT street_address, city, location, capitol, country_name 
FROM locations 
NATURAL JOIN countries; 

/*
Задача 2 
Отделу кадров необходим отчёт обо всех сотрудниках. Создайте запрос, чтобы отобразить фамилии, номера отделов и названия отделов для всех сотрудников. 
*/
SELECT last_name, department_id, department_name 
FROM employees 
NATURAL JOIN departments; 

/*
Задача 3 
Отделу кадров необходим отчёт обо всех сотрудниках в Торонто. Отобразите фамилию, должность,
номер отдела и название отдела для всех сотрудников, которые работают в Торонто. 
*/
SELECT last_name, job_id, department_id, department_name 
FROM employees 
NATURAL JOIN departments D 
JOIN locations L ON D.location_id = L.location_id 
WHERE city = 'Toronto'; 

/*
Задача 4 
Создайте отчёт, чтобы отобразить фамилии сотрудников и номера сотрудников наряду с фамилиями их начальников и номерами начальников. 
Назовите поля Employee, Emp#, Manager и Mgr#, соответственно. 
*/
SELECT emp1.last_name AS "Employee", emp1.employee_id AS "Emp#", emp2.last_name AS "Manager", emp2.manager_id AS "Mgr#" 
FROM employees emp1  
JOIN employees emp2 ON emp1.manager_id = emp2.employee_id 
ORDER BY emp2.employee_id; 

/*
Задача 5 
Измените задание 4, чтобы отобразить всех сотрудников, включая King, у которых нет начальника. Отсортируйте результат по номеру сотрудника.  
*/
SELECT emp1.last_name AS "Employee", emp1.employee_id AS "Emp#", emp2.last_name AS "Manager", emp2.manager_id AS "Mgr#" 
FROM employees emp1  
LEFT JOIN employees emp2 ON emp1.manager_id = emp2.employee_id 
ORDER BY "Emp#"; 

/*
Задача 6 
Создайте отчёт для отдела кадров, чтобы отобразить фамилии сотрудников, номера отделов и всех коллег сотрудников. Дайте каждому полю соответствующее название. 
*/
SELECT dep.department_id, emp1.last_name EMPLOYEE, emp2.last_name COLLEAGUE 
FROM employees emp1 
JOIN departments dep ON dep.department_id = emp1.department_id 
JOIN employees emp2 ON emp1.department_id = emp2.department_id 
WHERE emp1.employee_id != emp2.employee_id 
ORDER BY dep.department_id; 

/*
Задача 7 
Отдел кадров нуждается в отчете относительно рабочих категорий и зарплат. Чтобы ознакомить себя с таблицей  JOB_GRADES, 
сначала покажите структуру таблицы JOB_GRADES. Создайте запрос, который показывает имя, должность, название отдела, зарплату, 
и рабочую категорию для всех сотрудников. 
*/
SELECT emp.last_name, emp.job_id, dep.department_name, emp.salary, gr.grade_level 
FROM employees emp  
JOIN departments dep ON dep.department_id = emp.department_id 
JOIN job_grades gr ON emp.salary BETWEEN gr.lowest_sal AND gr.highest_sal; 

/*
Задача 8 
Отдел кадров хочет определить имена всех служащих, которые были приняты на работу после Davies. 
Создайте запрос, чтобы отобразить имя и дату приема на работу любого сотрудника, принятого после сотрудника Davies. 
*/
SELECT emp1.first_name AS "Employee", emp1.hire_date 
FROM employees emp1  
JOIN employees emp2 ON (emp1.hire_date > emp2.hire_date)  
WHERE emp2.last_name = 'Davies'  
ORDER BY emp1.hire_date;

/*
Задача 9 
Отдел кадров должен найти имена и даты приема всех сотрудников, которые были наняты перед их начальниками, наряду с именами их начальников и датами приема. 
*/
SELECT emp1.first_name, emp1.hire_date, emp2.first_name, emp2.hire_date 
FROM employees emp1 
JOIN employees emp2 ON (emp1.hire_date < emp2.hire_date) 
WHERE emp1.employee_id = emp2.manager_id; 