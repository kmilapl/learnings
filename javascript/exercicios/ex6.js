//06) Elabore duas funções que recebem três parâmetros: capital inicial, taxa de juros e tempo de aplicação. A
//primeira função retornará o montante da aplicação financeira sob o regime de juros simples e a segunda
//retornará o valor da aplicação sob o regime de juros compostos.

function a(capitalInicial, taxaDeJuros, tempoAplicacao){
    let m = capitalInicial + (capitalInicial * taxaDeJuros * tempoAplicacao)
    return m 
}

function b(capitalInicial, taxaDeJuros, tempoAplicacao){
    let j = capitalInicial * (1 + taxa) ** tempo
}

console.log(a(5, 6, 7))

