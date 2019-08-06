# 牛牛找工作
def zom(dic,m):
    key = sorted(dic)
    for i in range(len(key)):
        if i==len(key)-1:
            if m>=key[i]:
                return (dic[key[i]])
                break
        elif m>=key[i] and m<key[i+1]:
            return (dic[key[i]])
            break
if __name__ == "__main__":
    a1 = list(map(int,input().split()))
    N,M = a1[0],a1[1]
    dic = {}
    for i in range(N):
        lis1 = list(map(int,input().split()))
        dic[lis1[0]]=lis1[1]  
    lis2 = list(map(int,input().split())) 
    for i in lis2:
        print(zom(dic,i))
