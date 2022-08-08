#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

if letra.isalpha():
    if (letra == 'a'):
        print("A letra ", letra, "é uma vogal!")
elif (letra == 'A'):
    print("A letra ", letra, "é uma vogal!")
elif (letra == 'e'):
    print("A letra ", letra, "é uma vogal!")
elif (letra == 'E'):
    print("A letra ", letra, "é uma vogal!")
elif (letra == 'i'):
    print("A letra ", letra, "é uma vogal!")
elif (letra == 'I'):
    print("A letra ", letra, "é uma vogal!")
elif (letra == 'o'):
    print("A letra ", letra, "é uma vogal!")
elif (letra == 'O'):
    print("A letra ", letra, "é uma vogal!")
elif (letra == 'u'):
    print("A letra ", letra, "é uma vogal!")
elif (letra == 'U'):
    print("A letra ", letra, "é uma vogal!")
elif (letra == int):
    print(input("Isso não é uma letra, digite novamente: "))
else:
    print("A letra", letra, "é uma consoante!")