'''华为机考第三题，动态规划，最长公共子序列
假设A中有n个元素，B中有m个元素。若A[m-1]==B[n-1],那么A[:m]和B[:n]的
最长公共子序列就是A[:m-1]和B[:n-1]的最长公共子序列长度+1
若A[m-1]!=B[n-1],那么A[:m]和B[:n]的最长公共子序列就是
max(A[:m-1]和B[:n]的最长公共子序列，A[:m]和B[:n-1]的最长公共子序列)'''
def lcs(A,B):
    dp = [['' for i in range(len(B))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B)):          
            if A[i] == B[j]:
                if i==0 or j==0:
                    dp[i][j] = A[i]
                else:
                    dp[i][j] = dp[i-1][j-1]+A[i]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1],key=len)
    for i in dp:
        print(i)
    return (dp[-1][-1])
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            A = input().split()
            B = input().split()
            print(len(A)-len(lcs(A,B)))
        except:
            break