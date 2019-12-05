#右下三角格式输出九九乘法表
# n = int(input())
n=9
for i in range(1,n+1):
    for k in range(1,n+1-i):
        print(end="       ")
    for j in range(1,i+1):
        product=i*j
        print("%d*%d=%2d" % (i,j,product),end=" ")
    print()