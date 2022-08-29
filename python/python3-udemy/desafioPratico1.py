"""
* Criar variáveis para nome (str), idade (int), altura (float), e peso (float) de uma pessoa.
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Camila'
idade = 23
altura = 1.50
peso = 48
anoAtual = 2022
anoNascimento = (anoAtual - idade)
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade. Ela tem {altura:.2f} de altura e pesa {peso}kls. Seu ano de nascimento é {anoNascimento} e seu imc é: {imc:.2f}')
