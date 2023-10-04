# Write your MySQL query statement below
SELECT name ,bonus FROM (SELECT A.name, B.bonus FROM Employee A LEFT JOIN  Bonus B ON A.empId = B.empId) AS SubqyeryALias WHERE bonus<1000 OR bonus IS NULL ;