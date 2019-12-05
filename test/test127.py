# ?改 0 1 
import copy
def xxx(arr):
    for i in range(len(arr)):
        if arr[i] == '?':
            arr1 = copy.deepcopy(arr)
            arr2 = copy.deepcopy(arr)
            arr1[i] = 0
            arr2[i] = 1           
            break
    flag = False
    if '?' in arr1 or '?' in arr2:
        flag = True
    if flag == True:
        xxx(arr1)
        xxx(arr2)
    else:
        print("".join(list(map(str,arr1))))
        print("".join(list(map(str,arr2))))
if __name__ == '__main__':
    arr = [1,1,1,0,0,'?','?','?',1]
    xxx(arr)
    