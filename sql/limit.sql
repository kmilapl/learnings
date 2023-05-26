--limita o numero de linhas da consulta
--muito utilizado na etapa de exploração dos dados
--muito utilizado em conjunto com order by

--1º exercicio
select *
from sales.funnel
limit 10

--2º exercicio
select *
from sales.products
order by price desc
limit 10
