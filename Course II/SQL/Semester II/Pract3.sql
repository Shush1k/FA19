/*
Задача 1 
Создайте запрос, чтобы показать текущую дату. Отобразите поле Дата.  
*/
SELECT SYSDATE 
FROM employees; 

/*
Задача 2 
Отдел  нуждается в отчете, который показывает номер сотрудника, фамилию, зарплату, и увеличение зарплаты на 15.5 % (выраженная в целом числе)
для каждого сотрудника. Озаглавьте поле New Salary. 
*/
SELECT employee_id, last_name, salary, ROUND(salary + salary * 0.155) AS "New Salary" 
FROM employees; 

/*
Задача 3 
Измените свой запрос, чтобы добавить поле, которое вычитает старую зарплату из новой зарплаты. Озаглавьте поле Increase. Выполните запрос. 
*/
SELECT employee_id, last_name, salary, ROUND(salary + salary * 0.155) AS "New Salary", ROUND(salary + salary * 0.155)-salary AS "Increase" 
FROM employees; 

/*
Задача 4.1 
Напишите запрос, который показывает фамилию (с первыми прописными буквами и всеми другими строчными буквами) и длину фамилии для всех сотрудников, 
фамилия которых начинается с букв J, A, или М. Дайте каждому полю соответствующую метку. Отсортируйте результаты по фамилии сотрудников. 
*/
SELECT UPPER(SUBSTR(last_name,1,1))||LOWER(SUBSTR(last_name,2)) last_name, LENGTH(last_name) AS LEN_LAST_NAME 
FROM employees 
WHERE SUBSTR(last_name,1,1) IN ('A', 'J', 'M')
ORDER BY last_name; 

/*
Задача 4.2 
Перепишите запрос так, чтобы пользователь был вынужден ввести букву, с которой начинается фамилия. 
Например, если пользователь вводит H, то результат должен показать всех сотрудников, фамилия которых начинается с буквы H. 
*/
SELECT INITCAP(last_name), LENGTH(last_name) AS LEN_LAST_NAME 
FROM employees  
WHERE SUBSTR(last_name, 1, 1) = :f

/*
Задача 4.3 
Перепишите запрос так, чтобы пользователь был вынужден ввести букву, с которой начинается фамилия. Например, если пользователь вводит h, то результат должен показать всех сотрудников, фамилия которых начинается с буквы H. 
*/
SELECT INITCAP(last_name), LENGTH(last_name) as LEN_LAST_NAME  
FROM employees  
WHERE last_name LIKE CONCAT(UPPER(:name),'%')  
ORDER BY last_name 

/*
Задача 5 
Отдел кадров хочет найти время работы каждого сотрудника. Для каждого сотрудника, покажите фамилию и вычислите число месяцев 
между сегодня и датой приема на работу. Озаглавьте поле MONTHS_WORKED. Отсортируйте результат по количеству рабочих месяцев. 
Округлите количество месяцев до самого близкого целого числа.  
*/
SELECT last_name, ROUND((SYSDATE - hire_date)/30) AS MONTHS_WORKED 
FROM employees 
ORDER BY MONTHS_WORKED; 

/*
Задача 6 
Создайте отчет, который отображает следующее сообщение для каждого сотрудника: <employee last name> earns <salary> monthly but wants <3 times salary>. 
Озаглавьте поле Dream Salaries. 
*/
SELECT last_name ||' earns '|| salary ||' monthly but wants '|| salary * 3 AS "Dream Salaries"  
FROM employees; 

/*
Задача 7
Отобразите фамилию каждого сотрудника, дату приема на работу, и дату выплаты зарплаты, которая является первым понедельником после шести месяцев работы. 
Озаглавьте поле REVIEW. Отформатируйте даты, чтобы дата отображалась в формате, подобном “понедельник, тридцать первого июля 2000.” 
*/
SELECT last_name, TO_CHAR(hire_date, 'YYYY-MON-DD', 'NLS_DATE_LANGUAGE = RUSSIAN') "hire",  
TO_CHAR(NEXT_DAY(ADD_MONTHS(hire_date, 6), 'monday'), 'day, dd month yyyy','NLS_DATE_LANGUAGE = RUSSIAN') REVIEW 
FROM employees; 

/*
Задача 8 
Отобразите фамилию, дату приема на работу, и день недели, в которую начал работу сотрудник. Озаглавьте поле DAY. 
Отсортируйте результаты по дням недели, начиная с понедельника.  
*/
SELECT last_name, TO_CHAR(hire_date, 'YYYY-MON-DD') "hire", TO_CHAR(hire_date, 'DAY') "day" 
FROM employees 
ORDER BY TO_CHAR(hire_date,'D'); 

/*
Задача 9 
Создайте запрос, который показывает фамилии сотрудников и процент комиссионных. Если сотрудник не получает комиссионные, отобразите “No Commission.” 
Озаглавьте поле COMM. 
*/
SELECT last_name, NVL(TO_CHAR(commission_pct, '.99'), 'No Commission.') COMM 
FROM employees; 

/*
Задача 10 
Создайте запрос, который показывает первые восемь символов фамилий сотрудников и указывает количество их зарплат со звездочками. 
Каждая звездочка показывает тысячу долларов. Отсортируйте данные в порядке убывания зарплаты. Озаглавьте поле EMPLOYEES_AND_THEIR_SALARIES. 
*/
SELECT last_name||RPAD(' ', ROUND(salary/1000)+1,'*') EMPLOYEES_AND_THEIR_SALARIES
FROM employees  
ORDER BY salary DESC; 

/*
Задача 11 
Используя функцию DECODE, напишите запрос, который отображает уровень всех сотрудников, основанных на значениях поля job_id, используя следующие данные: 
*/
SELECT job_id, 
DECODE (job_id, 'AD_PRES', 'A', 'ST_MAN', 'B', 'IT_PROG', 'C', 'SA_REP', 'D', 'ST_CLERK', 'E', '0') GRADE 
FROM employees; 