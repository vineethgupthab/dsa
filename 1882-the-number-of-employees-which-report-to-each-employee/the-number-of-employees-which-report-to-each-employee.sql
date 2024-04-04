-- Write your PostgreSQL query statement below
with managers as
(
SELECT reports_to, COUNT(employee_id) OVER(PARTITION BY reports_to) as reports_count,
     AVG(age) OVER(PARTITION BY reports_to) as average_age FROM employees
)
SELECT distinct b.employee_id, b.name, a.reports_count, ROUND(average_age) as average_age FROM managers a
JOIN employees b ON a.reports_to=b.employee_id
WHERE a.reports_to is not null and a.reports_count>=1
ORDER BY b.employee_id ASC