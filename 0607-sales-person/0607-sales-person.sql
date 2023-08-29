# Write your MySQL query statement below
select s.name from orders o
join Company c on o.com_id = c.com_id and c.name = 'RED'
right join SalesPerson s on o.sales_id = s.sales_id
where o.sales_id is null