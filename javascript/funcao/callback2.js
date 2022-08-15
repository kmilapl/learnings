const notas = [7.7, 6.5, 5.2, 8.9, 3.6, 7.1, 9.0]

//sem o callback
const notasBaixas1 = []
for (let i in notas) { //i: indice
    if (notas[i] < 7) {
        notasBaixas1.push(notas[i])
    }
}

console.log(notasBaixas1)

//com callback
const notasBaixas2 = notas.filter(function (nota) {  //filtrar os elementos de um array em cima de um determinario criterio (true ou false)
    return nota < 7
})

console.log(notasBaixas2)

const notasBaixas3 = notas.filter( nota => nota < 7)
console.log(notasBaixas3)