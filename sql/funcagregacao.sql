--executa operações aritméticas nos registros de uma coluna

--tipos:
-- COUNT()
-- SUM()
-- MIN()
-- MAX()
-- AVG() --média

select COUNT(*)
from sales.funnel


select count(paid_date)
from sales.funnel


select count(distinct product_id)
from sales.funnel
where visit_page_date between '20210101' and '20210131'


select min(price), max(price), avg(price)
from sales.products


select max(price)
from sales.products

select *
from sales.products
where price = (select max(price) from sales.products)