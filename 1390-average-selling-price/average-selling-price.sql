-- Write your PostgreSQL query statement below
with cte as
(
    SELECT a.product_id as product_id, start_date, end_date, units:: FLOAT, price*units:: FLOAT as total_val FROM Prices a
    LEFT JOIN Unitssold b ON a.product_id=b.product_id and b.purchase_date>=a.start_date and b.purchase_date<=a.end_date
)
, cte2 as
(
    SELECT product_id, COALESCE(SUM(total_val)/SUM(units),0) as average_price
    FROM cte
    GROUP BY product_id
)
SELECT product_id, ROUND(average_price::NUMERIC,2) as average_price FROM cte2
ORDER BY product_id ASC
