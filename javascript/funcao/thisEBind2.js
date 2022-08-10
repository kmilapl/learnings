//solução que armazena o this em uma constante e depois vc usa a constante

function Pessoa() {
    this.idade = 0

    const self = this //self significa que não vai mudar NUNCA
    setInterval(function (){
        self.idade++
        console.log(self.idade)
    }/*.bind(this)*/, 1000) // setInterval: dispara outra função a partir de determinado intervalo que vc passou (x milissegundos vai executando)
}

new Pessoa