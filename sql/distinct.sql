select brand
from sales.products --333 linhas

--remove linhas repetidas e mantém somente as distintas
--muito utilizado em exploração dos dados
--caso mais de uma coluna seja selecionada, esse comando irá retornar todas as combinações distintas.
select distinct brand
from sales.products --40 linhas

select distinct brand, model_year
from sales.products