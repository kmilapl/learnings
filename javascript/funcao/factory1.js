/* const prod1 = {
    nome: '...',
    preco: 45
}

const prod2 = {
    nome: '...',
    preco: 45
}
*/

//Factory simples
//Função que no final sempre retorna um novo objeto
function criarPessoa() {
    return{
        nome: 'Ana',
        sobrenome: 'Silva'
    }
}

console.log(criarPessoa())