const escola = "Cod3r"

console.log(escola.charAt(4)) //Resultado letra "r", C = 0 e ultima letra é o 4.
console.log(escola.charCodeAt(3)); //Resultado Unicode 51
console.log(escola.indexOf('3')); //3 de "Cod3r"

console.log(escola.substring(1)); //Resultado mostrando a partir do index 1 "od3r", C não mostra pq é o 0
console.log(escola.substring(0,3)); //Resultando mostrando somente index 0 á 2 "Cod" o 3 e 4 não mostra. (Va do indice 0 e me dê 3 caracteres)

//Concatenação
console.log('Escola '.concat(escola).concat("!")); //Resultado> EscolaCod3r!

//Replace
console.log(escola.replace(3, 'e')); //Resultado substitui o 3 pela letra "e"

console.log('Ana,Maria,Pedro'.split(',')); //Cria array separando por virgula [ 'Ana', 'Maria', 'Pedro' ]
