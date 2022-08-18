const pilotos = ['Vettel', 'Alonso', 'Raikkonen', 'Massa']
pilotos.pop() // massa quebrou o carro (pop remove o ultimo elemento do array)
console.log(pilotos)

pilotos.push('Verstappen')
console.log(pilotos)

pilotos.shift() //remove o primeiro elemento da lista
console.log(pilotos)

pilotos.unshift('Hamilton') //adiciona um elemento em primeiro na lista
console.log(pilotos)

//splice pode adc ou remover elementos

//adc
pilotos.splice(2, 0, 'Bottas', 'Massa')
console.log(pilotos)

//remover
pilotos.splice(3, 1) // massa quebrou 
console.log(pilotos)

const algunsPilotos1 = pilotos.slice(2) //novo array (pega um novo array a partir do indice indicado)
console.log(algunsPilotos1)

const algunsPilotos2 = pilotos.slice(1, 4) //indice 1 ate 4, mas o 4 n entra
console.log(algunsPilotos2)