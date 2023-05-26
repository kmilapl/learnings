--une expressões simples em uma composta

--tipos
-- AND
-- OR
-- NOT
-- BETWEEN
-- IN
-- LIKE (matchs imperfeitos) ex todos que começam com ANA e o % (coringa) para pegar tudo depois que começa com ANA
-- ILIKE (inora letras maiusculas e minusculas)
-- IS NULL

select *
from sales.products
where price>= 100000 and price <= 200000
--ou
select *
from sales.products
where price BETWEEN 100000 and 200000



select *
from sales.products
where price < 100000 or price > 200000
--ou
select *
from sales.products
where price NOT between 100000 and 200000



select *
from sales.products
where brand = 'HONDA' or brand = 'TOYOTA' or brand = 'RENAULT'
--ou
select * 
from sales.products
where brand in ('HONDA', 'TOYOTA', 'RENAULT')



select distinct first_name
from sales.customers
where first_name = 'ANA'
-- correto:
select distinct first_name
from sales.customers
where first_name LIKE 'ANA%' --tudo que vem depois de ana, se quiser que venha antes, colocar o coringa antes




select distinct first_name
from sales.customers
where first_name ILIKE 'ana%' --podemos escrever de qualquer jeito, pois mesmo que os nomes estejam em maiusculo na coluna da tabela, o ilike ignora e trás



select *
from temp_tables.regions
where population IS NULL


