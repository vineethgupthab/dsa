-- Write your PostgreSQL query statement below
SELECT * FROM Cinema
WHERE MOD(id,2)!=0 and lower(description)!='boring'
ORDER BY rating DESC