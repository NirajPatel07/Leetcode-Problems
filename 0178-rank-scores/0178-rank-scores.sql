# Write your MySQL query statement below
select score,
dense_rank() over (order by score desc) as 'Rank'
from Scores