import math
if __name__ == '__main__':
    while True:
        try:
            print()
            print('输入n的值：')
            n = int(input())
            x = int(math.sqrt(n))
            w= []
            for i in range(1,x+1):
                w.append(i**2)
            dp = [float('Inf') for i in range(n+1)]
            dp[0] = 0
            xp = [[]]
            for i in range(n+1):
                xp[i] = i
            print(xp)
            for i in range(len(w)):
                for j in range(w[i],n+1):
                    dp[j] = min(dp[j],dp[j-w[i]]+1)
            print('%d最少可由%d个数的平方相加而成'%(n,dp[-1]))
            
        except Exception as e:
            print(e.args)
            break