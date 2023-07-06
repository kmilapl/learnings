-- views são visualizações (atalhos), aonde envolvem vários recursos para que a query não fique enorme e pra que consiga usa-la diversas vezes
-- criar ou atualizar views sem precisar usar o DROP VIEW

CREATE OR REPLACE VIEW vendas_por_cliente AS 
SELECT 
	cus.customer_id,
    cus.first_name,
    cus.last_name,
    pay.amount
FROM customer cus
JOIN payment pay
	ON cus.customer_id = pay.payment_id
ORDER BY pay.amount DESC