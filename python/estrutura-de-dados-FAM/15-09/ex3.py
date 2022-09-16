listaA = [4, 2, 7, 0, 1, 7, 4, 9]
print("Lista A =", listaA)
print("id=", id(listaA))
print()


listaA.remove(7)
print("listaA.remove(7) => Lista A =", listaA)
print("listaA.remove(1) => Lista A =", listaA.remove(1))
print("Lista A =", listaA)
print()

del(listaA[2])
print("del( listaA[2] ) => Lista A =", listaA)
print()

x = listaA.pop()
print(" x = listaA.pop() => x = ", x, "\tlistaA = ", listaA)
print(" listaA.pop() =>", listaA.pop(), "\tlistaA = ", listaA)

print()
print("id =", id(listaA))
