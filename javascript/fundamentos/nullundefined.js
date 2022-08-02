let valor // não inicializado
console.log(valor)

// console.log(nome) ------nem foi declarado

qualquer = null //ausencia de valor
console.log(qualquer)

// console.log(qualquer.toString()) //erro, pois a variavel é nula e não tem como ler

const produto = {}
console.log(produto.preco)
console.log(produto)

produto.preco = 3.50
console.log(produto)

produto.preco = undefined //evite atribuir undefined
console.log(!!produto.preco)
console.log(produto)

produto.preco = null //sem preço
console.log(!!produto.preco)
console.log(produto)