# ******************************动态规划问题*****************************
# 最大子序和
# arr = [-2,1,-3,4,-1,2,1,-5,4]
# dp =[0]*len(arr)
# for i in range(len(dp)):
#     dp[i] = max(arr[i],arr[i]+dp[i-1])
# print(max(dp))
# 打家劫舍
# arr = [2,7,9,3,1]
# dp = [0]*len(arr)
# dp[0] = arr[0]
# dp[1] = max(arr[0],arr[1])
# for i in range(2,len(dp)):
#     dp[i] = max(dp[i-1],dp[i-2]+arr[i])
# print(dp)
# 买卖股票的最佳时机
# arr = [7,1,5,3,6,4]
# minx = arr[0]
# dp = [0]*len(arr)
# for i in range(1,len(arr)):
#     dp[i] = max(dp[i-1],arr[i]-minx)
#     if arr[i] < minx:
#         minx = arr[i]
# print(dp)
# 使用最小花费爬楼梯
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# dp = []
# dp.append(cost[0])
# dp.append(cost[1])
# for i in range(2,len(cost)+1):
#     if i == len(cost):
#         dp.append(min(dp[i-1],dp[i-2]))
#     else:
#         dp.append(min(dp[i-1]+cost[i],dp[i-2]+cost[i]))
# print(dp)
# 比特位计数
# n = 10
# arr = [i for i in range(n+1)]
# dp = []
# dp.append(0)
# k = 0
# for i in range(1,n+1):
#     if i == 2**k:
#         dp.append(1)
#         k += 1
#     else:
#         dp.append(1 + dp[i-2**k])
# print(dp)
# 最小张数问题
# n = 21
# arr = [4,9]
# dp = [-1, -1, -1, -1, 1, -1, -1, -1, 2, 1]
# if n >= 10:
#     for i in range(10,n+1):
#         if (dp[i-4] == -1):
#             if (dp[i-9] != -1):
#                 dp.append(dp[i-9]+1)
#             else:
#                 dp.append(-1)
#         if (dp[i-4] != -1):
#             if (dp[i-9] == -1):
#                 dp.append(dp[i-4]+1)
#             else:
#                 dp.append(min(dp[i-4]+1,dp[i-9]+1))
# print(dp[n])
# 三角形最小路径和
# ****************
