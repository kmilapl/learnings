-- remove espaços 
SELECT TRIM('   Carros    ');

-- remove espaços da esquerda
SELECT LTRIM('   Carros                            Teste');

-- remove espaços da direita
SELECT RTRIM('          Carros                            Teste');

-- remover alguns caracteres específicos (dos lados)
SELECT TRIM(BOTH 'a' FROM 'aaaaMotoaaaa');

-- remover alguns caracteres específicos (do inicio)
SELECT TRIM(LEADING 'a' FROM 'aaaaMotoaaaa');

-- remover alguns caracteres específicos (do final)
SELECT TRIM(TRAILING 'a' FROM 'aaaaMotoaaaa');

-- localiza em qual ordem a letra está
SELECT LOCATE('o', 'Carros');

-- transformar em minúsculo
SELECT lcase('Carros');

-- transformar em maiúsculo
SELECT ucase('Carros');

-- contar quantas letras tem
SELECT length('Carros');

-- repetir a palavra
SELECT repeat('Carros', 4);