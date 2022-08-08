#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   o produto do dobro do primeiro com metade do segundo .
#   a soma do triplo do primeiro com o terceiro.
#   o terceiro elevado ao cubo.

num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe outro número inteiro: "))
nReal = int(input("Informe um número real: "))

resp1 = num1 * 2 * (num2 / 2)
print("O produto do dobro do primeiro com metade do segundo: ", resp1)

resp2 = num1 * 3 + nReal
print("A soma do triplo do primeiro com o terceiro: ", resp2)

resp3 = nReal * nReal * nReal
print("O terceiro elevado ao cubo: ", resp3)

