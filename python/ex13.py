#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#   Para homens: (72.7*h) - 58
#   Para mulheres: (62.1*h) - 44.7

altura = float(input("Informe a sua altura: "))
pesoMulher = (62.1 * altura) - 44.7
pesoHomem = (72.7 * altura) - 58

print("Caso seja mulher, seu peso ideal é: ", pesoMulher)
print("Caso seja homem, seu peso ideal é: ", pesoHomem)

