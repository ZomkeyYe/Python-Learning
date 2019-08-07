# 冒泡排序
def maopao(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
            print(arr)
    return arr
a = [3,2,1,4]
print(maopao(a))