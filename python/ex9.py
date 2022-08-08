#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

f = int(input("Informe a temperatura em graus Fahrenheit: "))
c = 5 * ((f-32) / 9)

print("A temperatura Fahrenheit transformada em graus Celsius é: ", c,"°C")