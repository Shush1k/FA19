-- Практика 12-13
/*Pract 7-1*/
-- Task 1
select *
from d_play_list_items, d_track_listings;

-- Task 2
SELECT *
FROM d_play_list_items d1, d_track_listings d2
WHERE d1.song_id = d2.song_id;

-- Task 3
SELECT d_songs.type_code, d_songs.title, d_types.description
FROM d_songs, d_types
WHERE d_songs.type_code = d_types.code;

-- Task 4
SELECT d_songs.type_code, d_songs.title, d_types.description
FROM d_songs, d_types
WHERE d_songs.type_code = d_types.code AND d_songs.id in (47, 48);

-- Task 5
SELECT *
FROM d_clients, d_events, d_job_assignments
WHERE d_clients.client_number = d_events.client_number 
AND d_events.id = d_job_assignments.event_id;

-- Task 6
SELECT d_track_listings.song_id, d_cds.title
FROM d_track_listings, d_cds
WHERE d_track_listings.cd_number = d_cds.cd_number;

/*Pract 7-2*/
-- Task 1
SELECT ev.name, pck.code
FROM d_events ev, d_packages pck
WHERE(ev.cost BETWEEN pck.low_range AND pck.high_range);

-- Task 2
SELECT emp.last_name, emp.salary, jg.grade_level
FROM employees emp, job_grades jg
WHERE emp.salary BETWEEN jg.lowest_sal AND jg.highest_sal;

-- Task 4
WHERE a.ranking >= g.lowest_rank AND a.ranking <= g.highest_rank

-- Task 7
SELECT cust.first_name ||' '|| cust.last_name "Customer Name", od.order_number, od.order_total, od.order_date
FROM f_customers cust
LEFT JOIN f_orders od ON cust.id = od.cust_id;

-- Task 8
SELECT employees.last_name, employees.department_id, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id;

-- Task 9
SELECT employees.last_name, employees.department_id, departments.department_name
FROM employees, departments
WHERE employees.department_id(+) = departments.department_id;

-- Task 10
SELECT employees.last_name, employees.department_id, departments.department_name 
FROM employees, departments WHERE employees.department_id = departments.department_id(+) 
UNION 
SELECT employees.last_name, employees.department_id, departments.department_name 
FROM employees, departments WHERE employees.department_id(+) = departments.department_id;

-- Task 11
SELECT d_cds.title , d_track_listings.song_id
FROM d_cds, d_track_listings
WHERE d_cds.cd_number = d_track_listings.cd_number(+);

/*Pract8-1*/
-- Task 2
SELECT ROUND(AVG(cost), 2) as "avg cost"
FROM d_events;

-- Task 3
SELECT TO_CHAR(ROUND(AVG(salary), 2), '$999999.99') as "avg salary"
FROM f_staffs
WHERE manager_id = 19;

-- Task 4
SELECT TO_CHAR(ROUND(SUM(salary), 2), '$999999.99') as "total salary"
FROM f_staffs
WHERE id in (12, 19);

-- Task 5
SELECT MIN(salary) "lowest salary", MAX(hire_date) "most recent hire date", MIN(last_name) "top last name", MAX(last_name) "bottom last name"
FROM employees
WHERE department_id in (50, 60);

-- Task 9
SELECT AVG(NVL(order_total, 0)) as "Average"
FROM f_orders
WHERE order_date BETWEEN TO_DATE('January 1, 2002', 'fmMonth DD, YYYY') 
AND TO_DATE('December 21, 2002', 'fmMonth DD, YYYY');

-- Task 10
SELECT MAX(hire_date) as "the last"
FROM employees;

/*Pract8-2*/
-- Task 1
SELECT COUNT(*)
FROM d_songs;

-- Task 2
SELECT COUNT(DISTINCT venue_id)
FROM d_events

-- Task 3
SELECT COUNT(song_id) AS "songs", COUNT(distinct cd_number)  "dist songs"
FROM d_track_listings;

-- Task 4
SELECT COUNT(email) "emails"
FROM d_clients;

-- Task 5
SELECT (COUNT(*) - COUNT(auth_expense_amt)) "partners"
FROM d_partners;

-- Task 7
SELECT TO_CHAR(ROUND(AVG(NVL(auth_expense_amt, 100000)), 2), '$999999.99') as "total"
FROM d_partners;

/*Pract9-1*/
-- Task 2
-- A
SELECT manager_id, AVG(salary)
FROM employees
GROUP BY manager_id
HAVING AVG(salary) < 16000;
-- B
SELECT COUNT(*)
FROM d_cds
WHERE cd_number < 93;
-- C
SELECT type_code, MAX(TO_NUMBER(REPLACE(duration,' min', ''))) || ' min' as "max duration"
FROM d_songs
WHERE duration IN('3 min', '6 min', '10 min') AND id < 50
GROUP BY type_code;

-- Task 3
SELECT track, MAX(song_id)
FROM d_track_listings
WHERE track IN (1, 2, 3)
GROUP BY track;

-- Task 5
SELECT ROUND(MAX(AVG(salary)),2) as "Max Value",
ROUND(MIN(AVG(salary)),2) "Min Value"
FROM employees
GROUP BY department_id;

-- Task 6
SELECT AVG(MAX(salary)) "Avg Max Salary"
FROM employees
GROUP BY department_id;
