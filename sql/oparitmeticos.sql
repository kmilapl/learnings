--executa operações matematicas
--utilizados pra criar colunas calculadas
--alias (pseudonimos) "as" para dar nome as colunas
--|| operador de adição que concatena strings

--tipos
-- +
-- -
-- *
-- /
-- ^
-- %
-- || --> não é um operador aritmético, faz adição de strings

select *
from sales.customers
limit 10


--se quiser criar o nome da coluna com espaços, utilizar aspas duplas
--strings dentro de aspas duplas identificam ser uma coisa só
select
	first_name,
	last_name,
	email,
	birth_date,
	(current_date - birth_date) / 365 as years_old
from sales.customers


select
	first_name,
	last_name,
	email,
	birth_date,
	(current_date - birth_date) / 365 as years_old
from sales.customers
order by years_old


select 
	first_name || ' ' || last_name as full_name,
	email,
	birth_date
from sales.customers