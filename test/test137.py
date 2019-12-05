import math
n = 19
lis = []
while n !=0:
    x = int(math.sqrt(n))
    lis.append(x**2)
    n -= x**2
print(lis)