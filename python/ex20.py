#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite a letra conforme seu sexo: ")

if (sexo == 'F'):
    print("Sexo: F - Feminino")
elif (sexo == 'f'):
    print("Sexo: F - Feminino")
elif (sexo == 'M'):
    print("Sexo: M - Masculino")
elif (sexo == 'm'):
    print("Sexo: M - Masculino")
else:
    print("Sexo Inválido")
