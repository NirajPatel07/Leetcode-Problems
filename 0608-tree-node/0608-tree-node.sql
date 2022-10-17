SELECT id , CASE WHEN p_id IS NULL THEN "Root"
WHEN id NOT IN (select DISTINCT p_id from Tree WHERE p_id IS NOT NULL) THEN "Leaf"
ELSE "Inner" END AS type 
FROM Tree
ORDER BY p_id;