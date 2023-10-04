# Write your MySQL query statement below
SELECT MAX(num) as num FROM (SELECT num , COUNT(num) as count FROM MyNumbers GROUP BY num ORDER BY num) AS ungabunga WHERE count=1 ;