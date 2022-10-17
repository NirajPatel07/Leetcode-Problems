SELECT v.customer_id , count(v.customer_id) AS count_no_trans 
FROM Visits as v LEFT JOIN Transactions AS t
ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL 
GROUP BY v.customer_id;