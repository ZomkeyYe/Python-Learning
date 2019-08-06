# 快速排序
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot =  arr[len(arr)//2]
    left = [value for value in arr if value < pivot]
    middle = [value for value in arr if value == pivot]
    right = [value for value in arr if value > pivot]
    return quickSort(left)+middle+quickSort(right)

print(quickSort([3,1,5,7,12,2,4]))
