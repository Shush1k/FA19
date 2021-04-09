/*Pract 6-1*/
-- Task 1
SELECT last_name, department_name 
FROM employees CROSS JOIN departments; 
 
-- Task 2
SELECT department_id, department_name, location_id, city 
FROM departments NATURAL JOIN locations; 
 
-- Task 3
SELECT department_id, department_name, location_id, city 
FROM departments NATURAL JOIN locations 
WHERE department_id in (20, 50); 
 
/*Pract 6-2*/
-- Task 1
SELECT department_id, department_name, location_id, city 
FROM departments d JOIN locations l USING(location_id) 
WHERE location_id = 1400; 
 
-- Task 2
SELECT song_id, cd_number, title, comments 
FROM d_cds JOIN d_track_listings USING (cd_number) 
JOIN d_play_list_items USING (song_id); 

-- Task 3
SELECT department_id, location_id, department_name, city
FROM departments JOIN locations USING (location_id)
WHERE department_id in (10, 20, 30) AND city = 'Seattle';

-- Task 4
SELECT region_id, region_name, country_name
FROM countries JOIN regions USING(region_id)
WHERE region_name LIKE '%America%';

-- Task 5
SELECT  e.first_name, e.last_name, e.hire_date, j.job_id, j.job_title, j.max_salary
FROM employees e JOIN jobs j ON e.job_id = j.job_id
WHERE j.max_salary > 12000;

-- Task 6
SELECT job_title, first_name, last_name, email
FROM employees e JOIN jobs j ON e.job_id = j.job_id
WHERE job_title = 'Stock Clerk';

-- Task 7
SELECT e.employee_id as "employee id", e.first_name as "employee first name", e.last_name as "employee last name", m.manager_id as "manager ID", m.first_name as "manager first name", m.last_name as "manager last name"
FROM employees e LEFT JOIN employees m ON e.manager_id = m.employee_id;

-- Task 8
SELECT d.location_id, l.city, d.department_name
FROM departments d JOIN locations l ON d.location_id = l.location_id
JOIN countries c ON l.country_id = c.country_id
WHERE c.country_name = 'Canada';

-- Task 9
SELECT e.manager_id as "manager id", e.department_id as "department id", d.department_name as "department name", e.first_name as "first name", e.last_name as "last name"
FROM  employees e JOIN departments d ON e.department_id = d.department_id
WHERE e.department_id in (80, 90, 110, 190);

-- Task 10
SELECT e.employee_id "employee id", e.last_name as "last name" , e.department_id as "department id", d.department_name as "department name", e.hire_date as "hire date"
FROM  employees e LEFT JOIN departments d ON e.department_id = d.department_id
WHERE e.hire_date = TO_DATE('June 7, 1994', 'fmMonth DD, YYYY');

/*Pract 6-3*/
-- Task 1
SELECT e.first_name as "First Name", e.last_name as "Last Name" , d.department_name as "Department Name" 
FROM  employees e LEFT JOIN departments d ON e.department_id = d.department_id; 
 
-- Task 2
SELECT e.first_name as "First Name", e.last_name as "Last Name" , d.department_name as "Department Name" 
FROM  employees e RIGHT JOIN departments d ON e.department_id = d.department_id; 
 
-- Task 3
SELECT e.first_name as "First Name", e.last_name as "Last Name" , d.department_name as "Department Name" 
FROM  employees e FULL JOIN departments d ON e.department_id = d.department_id; 
 
-- Task 4
SELECT c.first_name, c.last_name, e.event_date, e.description 
FROM  d_clients c LEFT JOIN d_events e USING(client_number); 
 
-- Task 5
SELECT s.description as "description", sa.shift_assign_date as "date" 
FROM  f_shifts s LEFT JOIN f_shift_assignments sa USING(code); 

/*Pract 6-4*/
-- Task 1
SELECT e.last_name as "Employee", e.employee_id as "Emp#", m.last_name as "Manager", m.employee_Id as "Mgr#" 
FROM employees e JOIN employees m ON e.manager_id=m.employee_id; 
 
-- Task 2
SELECT e.last_name as "Employee", e.employee_id as "Emp#", m.last_name as "Manager", m.employee_Id as "Mgr#" 
FROM employees e INNER JOIN employees m ON e.manager_id=m.employee_id 
ORDER BY "Employee"; 
 
-- Task 3
SELECT e.last_name as "Employee", e.hire_date as "Emp Hired", m.last_name as "Manager", m.hire_date as "Mgr Hired" 
FROM employees e LEFT JOIN employees m ON e.manager_id=m.employee_id 
WHERE e.hire_date < m.hire_date 
ORDER BY "Employee"; 
 
-- Task 4
SELECT last_name, salary, department_id 
FROM employees 
START WITH first_name ||' '|| last_name = 'Lex De Haan' 
CONNECT BY PRIOR employee_id = manager_id; 
 
-- Task 5
-- King is itself the tree base, connection priority must be changed
SELECT last_name, department_id, salary, employee_id, manager_id 
FROM employees 
START WITH last_name = 'King' 
CONNECT BY manager_id = PRIOR employee_id; 
 
-- Task 6
SELECT LPAD(last_name, LENGTH(last_name) + (LEVEL - 1) * 2, '—') as "organization chart" 
FROM employees 
START WITH last_name = (SELECT last_name from employees WHERE manager_id IS NULL) 
CONNECT BY PRIOR employee_id = manager_id; 
 
-- Task 7
SELECT LPAD(last_name, LENGTH(last_name) + (LEVEL - 1) * 2, '—') as "organization chart" 
FROM employees 
START WITH last_name = (SELECT last_name from employees WHERE manager_id IS NULL) 
CONNECT BY PRIOR employee_id = manager_id AND last_name != 'De Haan'; 