//Função sem retorno
function imprimirSoma(a, b) {
    console.log(a + b)
}

imprimirSoma(2, 3)
imprimirSoma(2) //NaN
imprimirSoma(2, 10, 4, 5, 6)
imprimirSoma()

//Função com retorno
function soma(a, b = 0) {
    return a + b
}
console.log(soma(2, 3)) //3 substitui o b, que tinha 0
console.log(soma(2)) //resultado é 2, pois o b pega o 0 definido na função