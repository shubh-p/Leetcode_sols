# Write your MySQL query statement below
SELECT DISTINCT A.num as ConsecutiveNums  from Logs A JOIN Logs B ON A.num=B.num AND A.id =B.id-1 JOIN Logs C  ON A.num=C.num  AND B.id=C.id-1;