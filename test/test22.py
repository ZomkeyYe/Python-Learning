a = [3, 1, 10, 9, 21, 35, 4, 6]
s = range(1, len(a))[::-1]
print(s)
for i in s:
    for j in range(i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)