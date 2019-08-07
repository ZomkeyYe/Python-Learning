# 快速排序
def quicksort(arr):
    if len(arr)<=1:
        return arr
    m = arr[len(arr)//2]
    middle = [arr[len(arr)//2]]
    first = [i for i in arr if i < m]
    last = [i for i in arr if i > m]
    return quicksort(first)+middle+quicksort(last)
arr = [4, 10, 2, 3, 12, 11, 13, 5, 6]
print(quicksort(arr))