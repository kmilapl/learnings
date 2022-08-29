nome = 'Luiz Otávio'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}') #.2f pontos flutuantes
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))