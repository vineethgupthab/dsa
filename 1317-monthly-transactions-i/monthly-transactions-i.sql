SELECT TO_CHAR(trans_date, 'yyyy-mm') AS month,
    country,
    COUNT(*) as trans_count,
    COUNT(1) FILTER (WHERE state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    COALESCE(SUM(amount) FILTER (WHERE state = 'approved'),0) AS approved_total_amount
FROM Transactions
GROUP BY month, country