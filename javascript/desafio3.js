//Desafio: Troca de Valores
//Objetivo: Trocar o valor da variável de tal forma que depois da troca, o valor da A irá valer 94 e a B irá valer 7.

var a = 7;
var b = 94; 
console.log(a);
console.log(b);

let temp = a;
a = b;
b = temp;
console.log(a);
console.log(b);

//Ou

[a,b] = [b,a]