# 二维数组查找
# a = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
# x = 5
def findx(arr,x):
    i = 0
    j = len(arr[0])-1
    while (i <len(arr)) & (j >= 0):
        print(arr[i][j])
        if arr[i][j] == x:
            return True
            break
        elif arr[i][j] < x:
            i += 1
        else:
            j -= 1
    return False