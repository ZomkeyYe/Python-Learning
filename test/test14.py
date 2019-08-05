def insertSort(arr):
    length = len(arr)
    for i in range(1,length):
        print(arr)
        x = arr[i]
        for j in range(i,-1,-1):
            # j为当前位置，试探j-1位置
            if x < arr[j-1]:
                arr[j] = arr[j-1]                
            else:
                # 位置确定为j
                break
        arr[j] = x
        print(arr)

arr = [54,26,93,17,77,31,44,55,20]
insertSort(arr)
print(arr)

