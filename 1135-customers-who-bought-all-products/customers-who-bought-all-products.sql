# Write your MySQL query statement below
SELECT customer_id FROM Customer AS C
LEFT JOIN Product AS P
ON P.product_key = C.product_key
GROUP BY C.customer_id
HAVING (COUNT(DISTINCT C.product_key)) = (SELECT COUNT(*) FROM Product)