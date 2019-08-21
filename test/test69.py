# 数组跳动
def zomkey(a):
    flag = False
    for i in range(len(a)):
        if a[i] >0:
            if a[i]>len(a)-i-1:
                flag = True       
        if a[i]<0:
            if a[i]+i < 0:
                flag = True
    if flag == True:
        print("true")
    else:
        print("false")
if __name__ == '__main__':
    lis = input()
    lis1 = lis[1:-1]   
    lis2 = list(map(int,lis1.split(",")))
    zomkey(lis2)