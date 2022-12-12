USE pds;
SELECT * FROM jobs LEFT JOIN employees ON employees.JOB_ID=jobs.JOB_ID;
SELECT * FROM jobs RIGHT JOIN employees ON employees.JOB_ID=jobs.JOB_ID;

--Змінився порядок представлення інформації у рядках
