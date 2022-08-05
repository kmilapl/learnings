function tratarErroELancar(erro) {
    throw new Error('Ocorreu um erro de processamento...')
}

function imprimirNomeGritado(obj) {
    try{
    console.log(obj.name.toUpperCase() + '!!!')
    } catch (e) {
        tratarErroELancar(e)
    }
}

const obj = {nome: 'Roberto'}
imprimirNomeGritado(obj)