# Write your MySQL query statement below

SELECT
    r.contest_id,
    ROUND(COUNT(r.user_id) * 100 / (SELECT COUNT(DISTINCT user_id) FROM Users), 2) AS percentage
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id;