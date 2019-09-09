# 简单迷宫问题
def migong(N,M,Matrix):
    i = 0
    j = 0
    lis = [[i,j]]
    while (i != N-1) or (j != M-1):
        if i < N-1 and Matrix[i+1][j] == 0:
            i += 1
            lis.append([i,j])
        elif j < M -1 and Matrix[i][j+1] == 0:
            j += 1
            lis.append([i,j])
    return lis
if __name__ == '__main__':
    while True:
        try:
            N,M = map(int,input().split())
            lis = []
            for i in range(N):
                lis.append(list(map(int,input().split())))
            path = migong(N,M,lis)
            for i in path:
                print("(%d,%d)"%(i[0],i[1]))
        except:
            break
    
            
            