-- Write your PostgreSQL query statement below
SELECT a.project_id, ROUND(AVG(experience_years),2) as average_years FROM Project a
JOIN Employee b ON a.employee_id=b.employee_id
GROUP BY a.project_id
ORDER BY project_id