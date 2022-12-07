USE pds;

ALTER TABLE employees DROP COLUMN Taxes;
/*ALTER TABLE employees ADD Taxes DECIMAL(6,2) DEFAULT 0 ;*/
/*UPDATE employees SET Taxes=0.15*salary;*/
SELECT * FROM employees;

/*INSERT INTO employees(Taxes) VALUES (salary*0.15);*/
/*SELECT * FROM employees*/
/*SELECT first_name, last_name, SALARY, SALARY*0.15 AS Taxes FROM employees;*/
/*SELECT first_name, last_name, salary From employee order by first_name;*/
