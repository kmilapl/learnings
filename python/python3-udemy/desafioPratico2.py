"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se esse número é par ou impar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

from curses.ascii import isdigit

num = input("Digite um número: ")

if num.isdigit():
    num = int(num)
else:
    print("Você não digitou um número inteiro.")

resto = num % 2

if resto == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é ímpar.')