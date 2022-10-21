def fatorial(n):
  if n == 0 :
    return 1
  else:
    return n*fatorial(n-1)

n = 10

for i in range(0, n +1):
  print(i, '! = ', fatorial(i))