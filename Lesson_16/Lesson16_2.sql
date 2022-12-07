USE pds;
SELECT first_name, last_name, salary, salary*0.15 AS Taxes FROM employees;

/* 
ПИТАННЯ ЛЕКТОРУ!!!
В чому помилка при роботі альтернативного скрипта??
ALTER TABLE employees ADD Tax DECIMAL(6,2) DEFAULT 0.15*salary ;

та альтернативного варианту
ALTER TABLE employees ADD Tax DECIMAL(6,2) DEFAULT 0 ;
UPDATE employees SET Tax=0.15*salary;
*/