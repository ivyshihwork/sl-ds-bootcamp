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

-- 10. Write a query to assign ranks to each employee based on their experience. 
-- Take data from the employee record table.

SELECT EMP_ID, FIRST_NAME, LAST_NAME, EXP, 
    RANK() OVER( ORDER BY EXP DESC) AS EXP_RANK
FROM EMP_RECORD_TABLE;


-- 11.  Write a query to create a view that displays 
-- employees in various countries whose salary is more than six thousand. 
-- Take data from the employee record table.

CREATE OR REPLACE VIEW SAL_OVER_6K_EMP_VW AS
    SELECT * FROM EMP_RECORD_TABLE
    WHERE SALARY > 6000;

SELECT * FROM SAL_OVER_6K_EMP_VW;

-- 12. Write a nested query to find employees with experience of more than ten years. 
-- Take data from the employee record table.

SELECT * FROM EMP_RECORD_TABLE
WHERE EXP > 10;

-- 13. Write a query to create a stored procedure to retrieve the details of the employees whose experience is more than three years. 
-- Take data from the employee record table.


CREATE PROCEDURE `getEmpExpOver3` ()
BEGIN
	SELECT * FROM EMP_RECORD_TABLE WHERE EXP > 3;
END 


call getEmpExpOver3();


-- 14. Write a query using stored functions in the project table to check whether the job profile assigned to each employee in the data science team matches the organization’s set standard.

-- The standard being:
-- For an employee with experience less than or equal to 2 years assign 'JUNIOR DATA SCIENTIST',
-- For an employee with the experience of 2 to 5 years assign 'ASSOCIATE DATA SCIENTIST',
-- For an employee with the experience of 5 to 10 years assign 'SENIOR DATA SCIENTIST',
-- For an employee with the experience of 10 to 12 years assign 'LEAD DATA SCIENTIST',
-- For an employee with the experience of 12 to 16 years assign 'MANAGER'.

CREATE DEFINER=`root`@`localhost` FUNCTION `RoleExpCheck`(eid varchar(5)) RETURNS int
BEGIN
	DECLARE ROLED VARCHAR(50);
    DECLARE EXPD INT;
	SELECT ROLE INTO ROLED FROM EMP_RECORD_TABLE WHERE EMP_ID = EID;
    SELECT EXP INTO EXPD FROM EMP_RECORD_TABLE WHERE EMP_ID = EID;
    
	CASE ROLED
		WHEN 'JUNIOR DATA SCIENTIST' THEN RETURN IF( EXPD <=2 , 1, 0);
		WHEN 'ASSOCIATE DATA SCIENTIST' THEN RETURN IF( EXPD BETWEEN 2 AND 5, 1, 0);
        WHEN 'SENIOR DATA SCIENTIST' THEN RETURN IF (EXPD BETWEEN 5 AND 10, 1, 0);
        WHEN 'LEAD DATA SCIENTIST' THEN RETURN IF (EXPD BETWEEN 10 AND 12, 1, 0);
        WHEN 'MANAGER' THEN RETURN IF (EXPD BETWEEN 12 AND 16, 1, 0);
		ELSE
			RETURN -1;
	END CASE;

use employee;
select RoleExpCheck('E001');    -- RETURN -1 SINCE IT'S CEO 
select RoleExpCheck('E010');    -- RETURN 1 SINCE ROLE MATCHES EXP

-- THIS SHOWS OTHE THAN CEO, EVERYONE IS WITHIN ROLE EXP RANGE.
SELECT EMP_ID, RoleExpCheck(EMP_ID) FROM EMP_RECORD_TABLE;

-- 15. Create an index to improve the cost and performance of the query to find the employee
--  whose FIRST_NAME is ‘Eric’ in the employee table after checking the execution plan.

EXPLAIN SELECT * FROM EMP_RECORD_TABLE WHERE FIRST_NAME='ERIC';