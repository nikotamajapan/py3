import random
n = int(input('n - '))
nc = 0

for i in range(0,n):
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 <1:
        nc += 1
pi = 4.0 * nc / n
print('PI = ',pi, sep=' ')