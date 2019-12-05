import math
# n = int(input())
n = 12
x = int(math.sqrt(n))
w= []
for i in range(1,x+1):
    w.append(i**2)
dp = [float('Inf') for i in range(n+1)]
dp[0] = 0
xp = [[] for i in range(n+1)]
for i in range(n+1):
    if i == 0:
        xp[i] = 0
    else:
        for j in range(1,i+1):
            xp[i].append(1)
print(xp)
for i in range(len(w)):
    for j in range(w[i],n+1):
        dp[j] = min(dp[j],dp[j-w[i]]+1)
print('%d最少可由%d个数的平方相加而成'%(n,dp[-1]))
print(dp)
for i in range(len(w)):
    for j in range(w[i],n+1):
        if dp[j] == dp[j-w[i]]+1:
            xp[j] = [w[j] for x in range(j//w[j])]

