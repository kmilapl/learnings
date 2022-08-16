//02) Os triângulos podem ser classificados em 3 tipos quanto ao tamanho de seus lados:
//Equilátero: Os três lados são iguais. Isósceles: Dois lados iguais. Escaleno: Todos os lados são diferentes.
//Crie uma função que recebe os comprimentos dos três lados de um triângulo e retorne sua classificação quanto
//ao tamanho de seus lados. (Neste exemplo deve-se abstrair as condições matemáticas de existência de um
//triângulo).

function triangulo(a, b, c){
    if (a == b && b == c) {
        console.log('Triângulo Equilátero, pois os três lados são iguais.')
    }
    else if (a == b || b == c || c == a) {
        console.log('Triângulo Isósceles, pois dois lados são iguais.')
    }
    else {
        console.log('Triângulo Escaleno, pois todos os lados são diferentes.')
    }
}

triangulo(1, 1, 1)
triangulo(1, 1, 3)
triangulo(2, 5, 6)