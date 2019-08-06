# 求连续子数组的最大和
def mmm(arr):
    lis = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            y = 0
            for x in range(i,j+1):
                y += arr[x]
            lis.append(y)
    if max(lis)>0:
        return (max(lis))
    else:
        return 0


if __name__ == "__main__":
    arr = list(map(int,input().split(",")))
    print(mmm(arr))
