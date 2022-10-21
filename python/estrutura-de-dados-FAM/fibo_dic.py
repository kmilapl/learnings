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

def fibo_dic(n, d):
  if n in d:
    return d[n]
  else:
    fib = fibo_dic(n-1, d) + fibo_dic(n-2, d)
    d[n] = fib
    return fib

d = {1:1, 2:1}
n = 10

print('finanacci(', n, ') : ', fibo_dic(n, d))