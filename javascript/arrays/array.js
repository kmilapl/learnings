console.log(typeof Array, typeof new Array, typeof [])

let aprovados = new Array('Bia', 'Carlos', 'Ana')
console.log(aprovados)

aprovados = ['Bia', 'Carlos', 'Ana']
console.log(aprovados[0]) //Bia, index 0
console.log(aprovados[1]) 
console.log(aprovados[2])
console.log(aprovados[3]) //undefined

aprovados[3] = 'Paulo'
aprovados.push('Abia')
console.log(aprovados.length) //push é o mais aprovado pra puxar elementos pro array
console.log(aprovados)

aprovados[9] = 'Rafael'
console.log(aprovados.length)
console.log(aprovados[8] === undefined)

console.log(aprovados)
aprovados.sort() //ordenar o array
console.log(aprovados)

delete aprovados[1]
console.log(aprovados[1])
console.log(aprovados)

aprovados = ['Bia', 'Carlos', 'Ana']
aprovados.splice(1, 1, 'Elemento1') //splice serve para adicionar 
//elementos, como tbm pra remover, ou adc e remover ao mesmo tempo
//1 param - indice
//2 param - quantidade de elementos que vc quer excluir a partir daquele indice
//3... param - quais vc quer adicionar
console.log(aprovados)