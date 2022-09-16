listaA = [1, 5, 6, 9]
listaB = [4, 7, 2]

print(" lista A =", listaA)
print(" lista B =", listaB)
print()

x = zip(listaA, listaB)
y = zip(listaA, listaB, listaA)
print("zip(listaA, listaB)          =>", list(x))
print("zip(listaA, listaB, listaA)  =>", list(y))

for i, j in zip(listaA, listaB):
    print("", i, "", j)
print()

for i, j in zip(listaA, listaB):
    print("", i + j)