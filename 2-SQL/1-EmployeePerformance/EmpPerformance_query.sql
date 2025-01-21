use employee;

-- 3. Write a query to fetch EMP_ID, FIRST_NAME, LAST_NAME, GENDER, and DEPARTMENT from the employee record table, 
-- and make a list of employees and details of their department.

SELECT  EMP_ID, FIRST_NAME, LAST_NAME, GENDER, DEPT AS DEPARTMENT FROM EMP_RECORD_TABLE ORDER BY DEPT;

-- 4. Write a query to fetch EMP_ID, FIRST_NAME, LAST_NAME, GENDER, DEPARTMENT, and EMP_RATING if the EMP_RATING is: 
-- less than two
-- greater than four 
-- between two and four

SELECT  EMP_ID, FIRST_NAME, LAST_NAME, GENDER, DEPT AS DEPARTMENT, EMP_RATING FROM EMP_RECORD_TABLE 
WHERE EMP_RATING <2;

SELECT  EMP_ID, FIRST_NAME, LAST_NAME, GENDER, DEPT AS DEPARTMENT, EMP_RATING FROM EMP_RECORD_TABLE 
WHERE EMP_RATING >4;

SELECT  EMP_ID, FIRST_NAME, LAST_NAME, GENDER, DEPT AS DEPARTMENT, EMP_RATING FROM EMP_RECORD_TABLE 
WHERE EMP_RATING BETWEEN 2 AND 4 ORDER BY EMP_RATING;

-- 5. Write a query to concatenate the FIRST_NAME and the LAST_NAME of employees in the Finance department from the employee table 
-- and then give the resultant column alias as NAME.

SELECT CONCAT(FIRST_NAME,' ', LAST_NAME) AS NAME FROM EMP_RECORD_TABLE 
WHERE DEPT='FINANCE';

-- 6. Write a query to list only those employees who have someone reporting to them. 
-- Also, show the number of reporters (including the President).
SELECT B.EMP_ID AS MANAGER_ID,COUNT(A.EMP_ID ) AS DIRECT_REPORT_COUNT FROM EMP_RECORD_TABLE A, EMP_RECORD_TABLE B 
WHERE A.MANAGER_ID = B.EMP_ID GROUP BY B.EMP_ID ORDER BY B.EMP_ID ;

-- 7. Write a query to list down all the employees from the healthcare and finance departments using union. 
-- Take data from the employee record table.

SELECT *  FROM EMP_RECORD_TABLE WHERE DEPT='FINANCE'
UNION DISTINCT 
SELECT * FROM EMP_RECORD_TABLE WHERE DEPT='HEALTHCARE';


-- 8. Write a query to list down employee details such as 
-- EMP_ID, FIRST_NAME, LAST_NAME, ROLE, DEPARTMENT, and EMP_RATING grouped by dept. 
-- Also include the respective employee rating along with the max emp rating for the department.

SELECT EMP_ID, FIRST_NAME, LAST_NAME, ROLE, DEPT, EMP_RATING, MAX(EMP_RATING) OVER( PARTITION BY DEPT) AS MAX_EMP_RATING 
FROM EMP_RECORD_TABLE;

-- 9. Write a query to calculate the minimum and the maximum salary of the employees in each role. 
-- Take data from the employee record table.

SELECT EMP_ID, FIRST_NAME, LAST_NAME, ROLE, SALARY, 
    MIN(SALARY) OVER( PARTITION BY ROLE) AS MIN_SALARY,
    MAX(SALARY) OVER( PARTITION BY ROLE) AS MAX_SALARY
FROM EMP_RECORD_TABLE ORDER BY ROLE, SALARY;

-- 10. Write a query to assign ranks to each employee based on their experience. Take data from the employee record table.
