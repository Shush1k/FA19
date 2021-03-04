
/*
Задача 1 
Найдите самую высокую, самую низкую зарплату, общую сумму и среднюю зарплату всех сотрудников. Озаглавьте поля Maximum, Minimum, Sum и Average, соответственно. 
Округлите Ваши результаты до самого близкого целого числа.
*/
SELECT MAX(salary) "Maximum", MIN(salary) "Minimum", SUM(salary) "Sum", ROUND(AVG(salary)) "Average" 
FROM employees;

/*
Задача 2 
Измените запрос так, чтобы рассчитать минимальную, максимальную зарплату, общую сумму и среднюю зарплату для каждой должности. Выполните запрос.
*/
SELECT MAX(salary) "Maximum", MIN(salary) "Minimum", SUM(salary) "Sum", ROUND(AVG(salary)) "Average" 
FROM employees
GROUP BY job_id;

/*
Задача 3 
Создайте запрос, чтобы отобразить количество сотрудников с одинаковыми должностями. 
*/
SELECT job_id, COUNT(employee_id) "Emp_Count" 
FROM employees 
GROUP BY job_id; 

/*
Задача 4 
Сделайте запрос из третьей задачи универсальным, добавив возможность ввода кода должности при запуске. 
*/
SELECT job_id, COUNT(employee_id) "Emp_Count" 
FROM employees 
WHERE job_id = :f 
GROUP BY job_id; 

/*
Задача 5 
Определите количество начальников, не перечисляя их.  Назовите поле Number of Managers. 
Подсказка: Используйте поле MANAGER_ID для определения количества начальников.  
*/
SELECT COUNT(DISTINCT(manager_id)) "Number of Managers" FROM employees; 

/*
Задача 6 
Найдите разницу между самой высокой и самой низкой зарплатой. Назовите поле DIFFERENCE. 
*/
SELECT (MAX(salary)-MIN(salary)) "DIFFERENCE" 
FROM employees; 

/*
Задача 7 
Создайте отчёт, который отображает номер начальника и зарплату самых низкооплачиваемых сотрудников у этих начальников. 
Исключите сотрудников, у которых нет начальника. Исключите группы, где минимальная зарплата $6,000 или меньше. 
Отсортируйте результат в нисходящем порядке по зарплате. 
*/
SELECT manager_id, MIN(salary) "MIN_SALARY"  
FROM employees  
WHERE manager_id IS NOT NULL GROUP BY manager_id 
HAVING MIN(salary)>=6000 
ORDER BY "MIN_SALARY" DESC; 

/*
Задача 8 
Отобразите общее количество сотрудников и количество сотрудников, нанятых в 1995, 1996, 1997 и  1998.  Создайте соответствующие заголовки полей. 
*/
SELECT COUNT(employee_id) "TOTAL", 
COUNT(DECODE(TO_CHAR(hire_date,'YYYY'),'1995',1995)) "1995", 
COUNT(DECODE(TO_CHAR(hire_date,'YYYY'),'1996',1996)) "1996", 
COUNT(DECODE(TO_CHAR(hire_date,'YYYY'),'1997',1997)) "1997", 
COUNT(DECODE(TO_CHAR(hire_date,'YYYY'),'1998',1998)) "1998" 
FROM employees;

/*
Задача 9 
Создайте матричный запрос, чтобы отобразить должность, зарплату для этой должности, основанной на номере отдела, и общую зарплату для этой должности,
для отделов 20, 50, 80 и  90, давая каждому полю соответствующий заголовок.
*/
SELECT job_id, 
NVL(SUM(DECODE(department_id, 20, salary)), 0) "Dep 20", 
NVL(SUM(DECODE(department_id, 50, salary)), 0) "Dep 50", 
NVL(SUM(DECODE(department_id, 80, salary)), 0) "Dep 80", 
NVL(SUM(DECODE(department_id, 90, salary)), 0) "Dep 90", 
( NVL(SUM(DECODE(department_id, 20, salary)), 0) + NVL(SUM(DECODE(department_id, 50, salary)), 0) 
+ NVL(SUM(DECODE(department_id, 80, salary)), 0) + NVL(SUM(DECODE(department_id, 90, salary)), 0) ) "TOTAL" 
FROM employees GROUP BY job_id; 