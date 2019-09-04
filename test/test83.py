# 打印漏斗
def xxx(N,lis,sy): 
    firstline = 3
    while firstline*2 < N:
        N = N - 2*firstline
        lis.append(firstline)
        lis.insert(0,firstline)
        firstline += 2
    for i in lis:
        print(" "*((lis[0]-i)//2)+sy*i)
    print(N)
if __name__ == '__main__':
    lisS = input().split()
    N = int(lisS[0])-1
    sy = lisS[1]
    lis = [1]
    xxx(N,lis,sy)