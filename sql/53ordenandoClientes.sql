SELECT
	cus.customer_id,
    cus.first_name as nome,
    cus.last_name as sobrenome,
    sum(amount) as total
    
FROM payment pay
JOIN customer cus USING(customer_id)

GROUP BY customer_id
ORDER BY total DESC