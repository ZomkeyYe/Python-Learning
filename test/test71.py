# 找出所找到质数十位数与个位数之和中的较小值
def zomkey(L,R):
    lis = []
    for i in range(L,R):   
        Flag = True     
        if i > 1:
            for j in range(2,i):                
                if i%j == 0:
                    Flag = False
                    break                                    
            if Flag == True:
                lis.append(i)
    # print(lis)
    lis1 = [i//10%10 for i in lis]
    lis2 = [i%10 for i in lis]
    # print(lis1)
    # print(lis2)
    return min(sum(lis1),sum(lis2))
if __name__ == '__main__':
    lis = list(map(int,input().split()))
    L,R = lis[0],lis[1]
    print(zomkey(L,R))