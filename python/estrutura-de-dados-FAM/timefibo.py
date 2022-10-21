import time 

def fibo(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fibo(n-1) + fibo(n-2)

def mostrar_serie_fibo(n):
  for n in range(1, n+1):
    print('finanacci(', n, ') : ', fibo(n))

n = 10
mostrar_serie_fibo(n)

def eficiencia(n):
  inicio = time.time()
  print('finanacci(', n, ') : ', fibo(n))
  fim = time.time()
  tempo_exec = (fim-inicio)

  print('{:.3f}s'.format(tempo_exec))

n = 10
eficiencia(n)
print("")

n = 30
eficiencia(n)
print("")