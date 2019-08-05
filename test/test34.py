def cnm(arr):
    print(arr)
    if len(arr)<=1:
        return arr[0]
    for i in range(1,len(arr)+1):
        if i%2 == 0:
            arr[i-1]=0
    arr = list(set(arr))
    arr.remove(0)
    return cnm(arr)
if __name__ == "__main__":
    n = 100
    arr = []
    for i in range(n):
        arr.append(i+1)
    print(cnm(arr))

