def divisao(x, y):
    q = x // y
    r = x % y
    return(q, r)

n = 5
d = 3

(rest_int, resto) = divisao(n, d)

print(n, '//',d,'=', rest_int)
print(n, '%',d,'=', resto)

n = 11
d = 4

(rest_int, resto) = divisao(n, d)

print(n, '//',d,'=', rest_int)
print(n, '%',d,'=', resto)
