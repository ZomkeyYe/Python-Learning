# 二分查找
from test55 import quicksort
def binarysearch(arr,x):
    first = 0
    last = len(arr)   
    while True:
        mid = (first+last)//2
        if arr[mid] == x:
            return mid
            break
        elif arr[mid]>x:
            last = mid - 1
        elif arr[mid]<x:
            first = mid + 1
        else:
            return -1
if __name__ == "__main__":
    arr = [4, 10, 2, 3, 12, 11, 13, 5, 6]
    arr1 = quicksort(arr)
    print(binarysearch(arr1,6))