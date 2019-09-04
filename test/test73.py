# 大小问题
def zom(a,b,c):
    if a+b > c:
        flag = "true" 
    else:
        flag = "false"
    return flag
if __name__ == '__main__':
    N = int(input())
    lis = []
    for i in range(N):
        lll = list(map(int,input().split()))
        a,b,c = lll[0],lll[1],lll[2]
        lis.append(zom(a,b,c))
    for i in range(N):
        print("Case #"+str(i+1)+": "+lis[i])