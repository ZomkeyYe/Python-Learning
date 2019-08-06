# 被3整除
def mmm(l,r):
    lis = []
    x = ''
    for i in range(l):
        x+=str(i+1)
    lis.append(int(x))
    for i in range(l,r):

        x+=str(i+1)
        lis.append(int(x))
    count = 0
    for i in lis:
        if i%3 == 0:
            count+=1
    print(count)

if __name__ == "__main__":
    lis = list(map(int,input().split()))
    l,r = lis[0],lis[1]
    mmm(l,r)