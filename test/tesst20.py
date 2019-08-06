# 水仙花数
sxh=[]
for i in range(100,1000):
    s = 0
    m = list(str(i))
    for n in m:
        s+= (int(n))**len(m)
    if i==s:
        sxh.append(i)
print("100-999中的水仙花数有：",end="")
print(sxh)

