
a = [2,5,8,3,9,1,6,4,7]
n = len(a)

for i in range(n):

    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]


print(a)