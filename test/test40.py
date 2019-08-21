# 被3整除
def mmm(l,r):
    lis = []
    x1 = int((l+1)*l/2)
    lis.append(x1)
    for i in range(l+1,r+1):
        x2 = lis[-1] + i
        lis.append(x2)
    count = 0
    # print(lis)
    for i in lis:
        if i%3 == 0:
            count+=1
    print(count)

if __name__ == "__main__":
    lis = list(map(int,input().split()))
    l,r = lis[0],lis[1]
    mmm(l,r)