# Write your MySQL query statement below

SELECT email FROM Person GROUP BY email having COUNT(*) > 1;