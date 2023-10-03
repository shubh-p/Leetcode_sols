# Write your MySQL query statement below
SELECT User_id , COUNT(DISTINCT follower_id) as followers_count FROM Followers GROUP BY user_id;