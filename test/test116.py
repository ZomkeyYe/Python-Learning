# **************************动态规划，多重背包问题**********************
def bagbag(w,v,n,c,l):
    w=[0]+w
    v=[0]+v
    l = [0]+l
    dp = [([0]*(c+1)) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,c+1):
            dp[i][j] = dp[i-1][j]
            for k in range(min(l[i],int(j/w[i]))+1):           
                if dp[i][j] < dp[i-1][j-k*w[i]]+k*v[i]:
                    dp[i][j] = dp[i-1][j-k*w[i]]+k*v[i]
    res = [0]*(n+1)
    m = n
    bag = c
    while m >= 1:
        i = m
        if dp[i][bag] == dp[i-1][bag]:
            res[i] = 0
        else:
            res[i] = 1
            bag -= w[i]
        m -= 1
    print("最大价值为： ",dp[n][c])
    print("所拿的物品为： ")
    count = 0
    for i in res[1:]:
        count += 1
        if i == 1:
            print("第"+str(count)+"件",end=" ")
if __name__ == '__main__':
    print("请输入物品个数：")
    n = int(input())
    print("请输入每个物品的价值：")
    v = list(map(int,input().split()))
    print("请输入每个物品的重量：")
    w = list(map(int,input().split()))
    print("请输入每个物品个数的限制：")
    l = list(map(int,input().split()))
    print("请输入背包的重量：")
    c = int(input())
    bagbag(w,v,n,c,l)
