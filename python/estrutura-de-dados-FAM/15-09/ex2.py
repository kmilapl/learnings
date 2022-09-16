listaA = [2, 1, 3]
print("Lista A =", listaA)


listaA.append(7)
print("listaA.append(7)=>\t Lista A =", listaA)


listaB = [9, 13, 20]
print()
print("Lista B =", listaB)
print()


listaC = listaA + listaB
print("listaC = listaA + listaB=>\t Lista C =", listaC)
print("Lista A =", listaA)
print("Lista B =", listaB)
print()


listaA.extend(listaB)
print("listaA.extend(ListaB)=>\t Lista A =", listaA)