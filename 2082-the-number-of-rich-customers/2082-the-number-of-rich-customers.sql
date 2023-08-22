# Write your MySQL query statement below

select COUNT(DISTINCT(customer_id)) as rich_count from Store where amount > 500;