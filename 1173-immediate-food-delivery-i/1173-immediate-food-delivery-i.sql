# Write your MySQL query statement below
select
round((select count(*) from Delivery where order_date = customer_pref_delivery_date) * 100 / (select count(*) from Delivery), 2) as immediate_percentage;