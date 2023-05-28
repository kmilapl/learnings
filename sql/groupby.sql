-- agrupa registros semelhantes de uma coluna
-- normalmente utilizado em conjunto com as funções de agregação

select state, count(*) as contagem
from sales.customers
group by state
order by contagem desc



select state, professional_status, count(*) as contagem
from sales.customers
group by state, professional_status
order by state, contagem desc



--funciona da mesma forma que distinct
select distinct state
from sales.customers

select state
from sales.customers
group by state