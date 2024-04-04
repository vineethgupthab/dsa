-- Write your PostgreSQL query statement below
with gather as
(
SELECT employee_id, department_id, LAST_VALUE(department_id) OVER(PARTITION BY employee_id ORDER BY department_id),primary_flag, COUNT(employee_id) OVER(PARTITION BY employee_id) as department_count from employee
)
SELECT employee_id, department_id FROM gather
WHERE primary_flag='Y' or department_count=1