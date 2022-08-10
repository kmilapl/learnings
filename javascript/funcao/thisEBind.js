const pessoa = {
    saudacao: 'Bom dia!',
    falar() {
        console.log(this.saudacao) //acessar o atributo de um objeto usando o this (se não usar o this, ele não reconhece)
    }
}

pessoa.falar()
const falar = pessoa.falar
falar() // conflito entre paradigmas: funcional e orientação a objetos

const falarDePessoa = pessoa.falar.bind(pessoa) //bind passa um objeto no qual vc quer que seja resolvido o this
falarDePessoa()