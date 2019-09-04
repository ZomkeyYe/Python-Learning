def zoo(lis):
    a1 = 0
    a2flag = False
    a2 = 0
    a3 = 0
    a4 = []
    a5 = []
    for i in lis:
        if i%5 == 0 and i%2 ==0:
            a1 += i
        if i%5 == 1:          
            if a2flag == False:
                a2 += i
                a2flag = True
            if a2flag == True:
                a2 -= i
                a2flag = False
            # print(a2flag)
        if i%5 == 2:
            a3 += 1
        if i%5 ==3:
            a4.append(i)
        if i%5 == 4:
            a5.append(i)
    print("{0} {1} {2} {3} {4}".format(a1,a2,a3,sum(a4)/len(a4),max(a5)))
if __name__ == '__main__':
    lis = list(map(int,input().split()))
    zoo(lis)