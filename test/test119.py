def migonggong(N,M,Q):
    while i < N and j < M:
        if i==0 and j==0:
            if Q[i][j]==0:
                return 0
        if Q[i][j] == 9:
            return 1
        if Q[i][j] == 1:  

           
    return 0
if __name__ == '__main__':
    while True:
        try:
            N,M = map(int,input().split())
            Q = []
            for i in range(N):
                Q.append(list(map(int,input().split())))
            if migonggong(N,M,Q):
                print("1")
            else:
                print("0")
        except Exception as e:
            print(e.args)
            break