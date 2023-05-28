-- serve pra filtrar linhas da seleção por uma coluna agrupada
-- tem a mesma função do where mas pode ser usado pra filtrar os resultados das funções agregadas enquanto o WHERE possui essa limitação

select
	state,
	count(*)
from sales.customers
group by state
having count(*) > 100


--funciona também pras funções não agregadas, não precisa usar somente where
select
	state,
	count(*)
from sales.customers
group by state
having count(*) > 100
	and state <> 'MG'
