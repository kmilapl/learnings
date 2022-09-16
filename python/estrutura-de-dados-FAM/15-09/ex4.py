listaA = [4, 2, 17, 0, 1, 3, 11, 9, 7]
print("Lista A =", listaA)
print(" id=", id(listaA), "\n")
listaA.sort()
print("listaA.sort() =>\t Lista A =", listaA)
print(" id=", id(listaA))
print()


listaA = [4, 2, 17, 0, 1, 3, 11, 9, 7]
print("Lista A =", listaA)
print(" id=", id(listaA), "\n")
listaB = sorted(listaA)
print(" listaB = sorted(listaA)")
print(" listaA = ", listaA, " id =", id(listaA))
print(" listaB = ", listaB, " id =", id(listaB))
print()

listaA= [4, 2, 17, 0, 1, 3, 11, 9, 7]
print("lista A =", listaA)
print(" id =", id(listaA), "\n")
listaA.reverse()
print("listaA.reverse() =>\t Lista A =", listaA)
print(" id =", id(listaA))
print()
