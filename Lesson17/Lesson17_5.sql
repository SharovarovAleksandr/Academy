USE pds;
SELECT  employees.first_name, employees.last_name, departments.department_name, departments.department_id, locations.city
FROM employees, departments, locations
WHERE employees.department_id=departments.department_id AND departments.location_id=locations.location_id AND locations.city='London';