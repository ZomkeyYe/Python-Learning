# 操作序列
if __name__ == "__main__":
    n = int(input())
    lis = []
    arr = list(map(int,input().split()))

    for i in range(len(arr)-1,-1,-2):
        lis.append(arr[i])
    if len(arr)%2==0:
        for i in range(0,len(arr),2):
            lis.append(arr[i])
    if len(arr)%2==1:
        for i in range(1,len(arr),2):
            lis.append(arr[i])
    lis = list(map(str,lis))
    x = " ".join(lis)
    print(x)
