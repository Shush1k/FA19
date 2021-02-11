-- Задание 6-3-1 
CREATE TABLE DEPT 

(   dept_id NUMBER(8) NOT NULL, 

    dept_name VARCHAR2(30) NOT NULL, 

    loc_id NUMBER(4) NOT NULL, 

    CONSTRAINT dept_pk PRIMARY KEY(dept_id, loc_id) 

); 

 

-- Задание 6-3-2 

CREATE TABLE SUPPLIERS 

(    sup_id NUMBER(15) NOT NULL 

    sup_name VARCHAR2(30) NOT NULL, 

    conract_name VARCHAR2(30) NOT NULL, 

    CONSTRAINT sup_pk PRIMARY KEY(sup_id, sup_name) 

); 

 

CREATE TABLE PRODUCT 

(    product_id NUMBER(10), 

     sup_id NUMBER(15), 

     sup_name VARCHAR2(30), 

     CONSTRAINT pdct_id_pk PRIMARY KEY (product_id), 

     CONSTRAINT pdct_id_name_fk FOREIGN KEY (sup_id,sup_name) 

     REFERENCES SUPPLIERS (sup_id,sup_name) 

); 

 

 
-- Задание 6-3-3 

CREATE TABLE DEPT_SAMPLE 

(   dept_id NUMBER(8) NOT NULL, 

    dept_name VARCHAR2(30) NOT NULL, 

    loc_id NUMBER(4) NOT NULL, 

    CONSTRAINT dept_uk UNIQUE(dept_id, dept_name) 

); 