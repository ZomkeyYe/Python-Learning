def zixulie(lis):
    if lis == []:
        return 0
    N = len(lis)
    dp=[1]*N
    for i in range(N):
        for j in range(i):
            if lis[i] >= lis[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)
if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            lis = list(map(int,input().split()))
            print(N-zixulie(lis))
        except:
            break