# 寻找给定区间内的回文素数
def zomkey(L,R):
    count = 0
    for i in range(L,R+1):
        Flag = True
        if i > 1:
            for j in range(2,i):                
                if i%j == 0:
                    Flag = False
                    break                                    
            if Flag == True:
                k = str(i)
                if k == k[::-1]:
                    print(i)
                    count += 1
    return count
if __name__ == '__main__':
    lis = list(map(int,input().split()))
    L,R = lis[0],lis[1]
    print(zomkey(L,R))