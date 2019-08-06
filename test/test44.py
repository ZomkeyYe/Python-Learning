# 数组排序
def mmm(arr1,arr2):
    arr3 = arr1+arr2
    arr3.sort()   
    print(','.join(map(str,arr3)))
if __name__ == "__main__":
    arr1 = list(map(int,input().split(",")))
    arr2 = list(map(int,input().split(",")))
    mmm(arr1,arr2)