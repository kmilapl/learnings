#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("Vamos calcular o seu salário do mês?")

valor = float(input("Informe quanto você ganha por hora: "))
horas = float(input("Informe o número de horas trabalhadas no mês: "))
salario = valor * horas

print("O seu salário do mês é de: R$",salario)