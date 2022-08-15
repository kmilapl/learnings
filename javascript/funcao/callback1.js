const fabricantes = ["Mercedes", "Audi", "BMW"]

function imprimir(nome, indice) {
    console.log(`${indice + 1}. ${nome}`)
}

//função callback pode ser chamada uma vez ou mais vezes, dependendo do contexto onde inserimos ela
//passa uma função pra outra e quando um determinado evento acontecer, essa função será chamada de volta

fabricantes.forEach(imprimir)
fabricantes.forEach(fabricante => console.log(fabricante)) //função arrow