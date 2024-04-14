WITH cte AS
(
    SELECT name as employee, departmentId, salary, 
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) 
    FROM Employee
)
SELECT name as Department, Employee, Salary FROM cte a
JOIN department b ON a.departmentId=b.id
WHERE dense_rank<4
ORDER BY salary DESC