SELECT
    CASE 
        WHEN id % 2 = 0 THEN id - 1
        WHEN id = (SELECT COUNT(*) FROM seat) THEN id
        ELSE id + 1
    END as id, student
FROM seat
ORDER BY id
