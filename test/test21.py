wqs=[]
for i in range(1,1000):
    s = 0
    for n in range(1,i):
        if i%n==0:
            s+=n
    if s==i:
        wqs.append(i)
print(wqs)
