with cte as 
(
    SELECT TO_CHAR(trans_date, 'YYYY-MM') as month, country, COUNT(*) as trans_count, COUNT(*) FILTER(WHERE state='approved') as approved_count, SUM(amount) as trans_total_amount, SUM(amount) FILTER(WHERE state='approved') as approved_total_amount FROM Transactions
GROUP BY month, country
)
SELECT month, country, trans_count, approved_count, COALESCE(trans_total_amount, 0) as trans_total_amount, COALESCE(approved_total_amount, 0) as approved_total_amount FROM cte