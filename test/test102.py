# 质数因子问题
n = int(input())
arr = []
for x in range(2,n//2+1):
    while n%x ==0:
        arr.append(x)
        n = n//x
if arr:
    for i in arr:
        print(i,end=" ")
else:
    print(str(n)+' ')
