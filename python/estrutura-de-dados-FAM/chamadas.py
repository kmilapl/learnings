def fibo(n):
  global numChamadas
  numChamadas += 1
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fibo(n-1) + fibo(n-2)

numChamadas = 0
print('\nFibonacci Recursão: ', fibo(12))
print('Chamadas da Função: ', numChamadas)


def fibo_dic(n, d):
  global numChamadas
  numChamadas += 1
  if n in d:
    return d[n]
  else:
    fib = fibo_dic(n-1, d) + fibo_dic(n-2, d)
    d[n] = fib
    return fib

numChamadas = 0
d = {1:1, 2:1}
print('\nFibonacci Recursão: ', fibo_dic(12, d))
print('Chamadas da Função: ', numChamadas)