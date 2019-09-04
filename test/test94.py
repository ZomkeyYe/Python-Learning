# 二分查找
def erfenchazhao(arr,x):
    fir = 0
    las = len(arr)- 1    
    while fir <= las:
        mid = (fir + las)//2
        if arr[mid] < x:
            fir = mid + 1
        if arr[mid] > x:
            las = mid -1
        if arr[mid] == x:
            return arr.index(arr[mid])+1      
    return len(arr)+1
if __name__ == '__main__':
    N,x = map(int,input().split())
    arr = list(map(int,input().split()))
    print(erfenchazhao(arr,x))
    