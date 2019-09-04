# 动态规划
import math

t = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# t = (2, 1, 6, 4, 5, 7, 4, 2, 5, 6, 1, 3, 2, 5)
arr = [1]
i = 1
maxLen = arr[0]
while i < len(t):
    temp = []
    j = 0
    boo = True
    while j < len(arr):
        if t[j] < t[i]:
            temp.append(arr[j])
            boo = False
        j += 1
    if boo:
        arr.append(1)
    else:
        arr.append(max(temp) + 1)
        if max(temp) + 1 > maxLen:
            maxLen = max(temp) + 1
    i += 1
print(arr)
print(maxLen)