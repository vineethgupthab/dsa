-- Write your PostgreSQL query statement below
with confirmed_table as
(
    SELECT a.user_id, COUNT(action)::FLOAT as confirmed_actions FROM Signups a
    JOIN Confirmations b ON a.user_id = b.user_id
    WHERE action='confirmed'
    GROUP BY a.user_id
)
, entries_table as
(
    SELECT a.user_id, COUNT(action)::FLOAT as all_actions FROM Signups a
    JOIN Confirmations b ON a.user_id = b.user_id
    GROUP BY a.user_id
)

SELECT c.user_id, COALESCE(ROUND(confirmed_actions::NUMERIC/all_actions::NUMERIC,2),0) as confirmation_rate FROM confirmed_table a
JOIN entries_table b ON a.user_id = b.user_id
RIGHT JOIN Signups c ON a.user_id = c.user_id
ORDER BY a.user_id
