WITH cte AS
(SELECT product_id FROM Sales
WHERE sale_date > '2019-03-31'
OR sale_date < '2019-01-01')

SELECT DISTINCT s.product_id , p.product_name
FROM Sales s
LEFT JOIN Product p
ON s.product_id=p.product_id  
WHERE s.product_id NOT 
IN(SELECT product_id FROM cte); 