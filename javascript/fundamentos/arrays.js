const valores = [7.7, 8.9, 6.3, 9.2]
console.log(valores[0], valores[3])

valores[4] = 10
console.log(valores)
console.log(valores.length) //qts elementos tem no array

valores.push({id: 3}, false, null, 'teste') //adiciona novos elementos no array
console.log(valores)

console.log(valores.pop()) //pega ultimo valor, tira e retorna
delete valores[0]
console.log(valores)

console.log(typeof valores)