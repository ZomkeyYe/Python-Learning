# 比较成绩
if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            lis = []
            for i in range(N):
                lis.append(input().split())
            for i in range(N):
                for j in range(0,N-i-1):
                    if int(lis[j][1]) < int(lis[j+1][1]):
                        lis[j],lis[j+1] = lis[j+1],lis[j]
                    if int(lis[j][1]) == int(lis[j+1][1]):
                        if int(lis[j][2]) > int(lis[j+1][2]):
                            lis[j],lis[j+1] = lis[j+1],lis[j]
            for i in range(N):
                print(lis[i][0])
        except:
            break


    