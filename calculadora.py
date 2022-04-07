print("\n******************* Calculadora Python: Camila Lira *******************")

def soma(x, y):
    return x + y

def subt(x, y):
    return x - y

def mult(x, y):
    return x * y

def divid(x, y):
    return x / y

print("\nSelecione o número da opção desejada: \n")
print("\n1- Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

opcao = input("Digite a sua opção (1/2/3/4): ")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if opcao == '1':
    print("A soma dos números é: ", soma(num1, num2))
    
elif opcao == '2':
    print("A subtração dos números é: ", subt(num1, num2))

elif opcao == '3':
    print("A multiplicação dos números é: ", mult(num1, num2))
    
elif opcao == '4':
    print("A divisão dos números é: ", divid(num1, num2))
    
else:
    print("\nVocê não digitou a opção corretamente!")