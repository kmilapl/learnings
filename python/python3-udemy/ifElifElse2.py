nome = input('Qual o seu nome?')
idade = input ('Qual a sua idade?')

idade = int(idade)

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar empréstimo.')
else:
    print(f'{nome} não pode pegar empréstimo.')