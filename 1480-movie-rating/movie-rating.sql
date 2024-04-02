-- Write your PostgreSQL query statement below
with reviewer_count as
(
    SELECT 
        user_id, count(user_id) as review_count FROM MovieRating
    GROUP BY user_id
),
most_reviewer as
(
    SELECT name FROM reviewer_count a
    JOIN users b ON a.user_id = b.user_id
    ORDER BY review_count DESC, lower(name) ASC
    LIMIT 1
),
feb_movie_rating as
(
    SELECT 
        movie_id, AVG(rating) as average_rating FROM MovieRating
    WHERE to_char(created_at,'MM-YYYY') = '02-2020'
    GROUP BY movie_id
)
, top_movie as
(
    SELECT title FROM feb_movie_rating a
    JOIN movies b on a.movie_id=b.movie_id
    ORDER BY average_rating DESC, lower(title) ASC
    LIMIT 1
)
SELECT name as results FROM most_reviewer
UNION ALL
SELECT title as results FROM top_movie