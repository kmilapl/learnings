#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print("Vamos calcular a área de um quadrado?")

lado = int(input("Insira o valor do lado do quadrado: "))
area = lado * lado
dobro = area * 2

print("A área do quadrado é: ", area)
print("O dobro dessa área é: ", dobro)