-- Write your PostgreSQL query statement below
WITH cte as 
(
SELECT *, ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) as first_order FROM Delivery
)
, cte2 as
(
SELECT CASE WHEN order_date=customer_pref_delivery_date THEN 1 ELSE 0 END as immediate FROM cte
WHERE first_order=1
) 
SELECT ROUND(SUM(immediate::NUMERIC)/COUNT(immediate::NUMERIC)*100,2) as immediate_percentage FROM cte2