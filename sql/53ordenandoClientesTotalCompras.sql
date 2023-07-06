SELECT
	cus.customer_id,
    cus.first_name as nome,
    cus.last_name as sobrenome,
    sum(amount) as total,
    count(amount) as compras
FROM payment pay
JOIN customer cus USING(customer_id)

GROUP BY customer_id
HAVING total >= 150 AND compras >= 35
ORDER BY total DESC