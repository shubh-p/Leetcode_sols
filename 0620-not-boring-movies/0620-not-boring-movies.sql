# Write your MySQL query statement below
SELECT * from Cinema WHERE id%2 = 1 and description != "boring" ORDER BY rating DESC;