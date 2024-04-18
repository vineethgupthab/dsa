-- Write your PostgreSQL query statement below

with cte as
(
    SELECT visited_on, SUM(amount) as amount FROM Customer
    GROUP BY visited_on
)
, cte2 as
(
    SELECT visited_on, SUM(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as total, AVG(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as average_amount, DENSE_RANK() OVER(ORDER BY visited_on ASC) FROM cte
)
SELECT visited_on, ROUND(total,2) as amount, ROUND(average_amount,2) as average_amount FROM cte2
WHERE dense_rank>6
