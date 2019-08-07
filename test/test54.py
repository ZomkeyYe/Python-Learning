# 插入排序
def charu(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1],arr[j] = arr[j],arr[j+1]
            j-=1
        print(arr)
    return arr
arr = [4, 10, 2, 3, 12, 11, 13, 5, 6]

print (charu(arr))