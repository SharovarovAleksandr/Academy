
USE pds;
SELECT JOB_ID, COUNT(JOB_ID)  FROM employees group by job_id;

