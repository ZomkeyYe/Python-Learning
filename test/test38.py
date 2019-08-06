# 最大乘积问题
def zom(arr):
    for i in range(len(arr)):
        amin = None
        for j in range(len(arr)-1):    
            if arr[j+1]<arr[j]:        
                arr[j],arr[j+1]=arr[j+1],arr[j]
    n1,n2,n3=arr[:3:1]
    m1,m2,m3=arr[-3::1]
    return max(m1*m2*m3,n1*n2*m3)              

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print(zom(arr))