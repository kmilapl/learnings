--comparam dois valors retornando TRUE ou FALSE
--muito utilizado em conjunto com a função WHERE pra filtrar linhas de uma seleção
--utilizado pra criar colunas flag que retornem true ou false

--tipos
-- =
-- >
-- <
-- >=
-- <=
-- <>

select
	customer_id,
	first_name,
	professional_status,
	(professional_status = 'clt') as client_clt
from sales.customers