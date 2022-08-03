//Escopo é o local onde a variável é visível/acessível
{
    {
        {
            {
                var sera = 'Será????'
                console.log(sera)
            }
        }
    }
}
console.log(sera)

//Escopo de uma variável dentro da função é apenas visível dentro da função
function teste() {
    var local = 123
    console.log(local)
}

teste()