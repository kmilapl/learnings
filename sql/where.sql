--filtrar linhas de tabela de acordo com uma condição
select email, state
from sales.customers
where state = 'SC'

select email, state, birth_date
from sales.customers
where (state = 'SC' or state = 'MS') and birth_date < '1991-12-28'