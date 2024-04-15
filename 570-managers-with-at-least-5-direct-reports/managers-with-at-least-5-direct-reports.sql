-- Write your PostgreSQL query statement below
with cte as 
(
    SELECT managerId, COUNT(managerId) as counts FROM Employee
    WHERE managerId is not NULL
    GROUP BY managerId
)

SELECT name FROM cte a
JOIN Employee b on a.managerId = b.id
WHERE counts>4