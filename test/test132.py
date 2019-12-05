def xxx(i,j):
    x = max(i,j)
    y = min(i,j)
    if x - y == 10 or x - y == 1:
        return True
    else:
        return False
if __name__ == '__main__':
    while True:
        try:
            A = list(map(int,input().split()))
            n = len(A)
            A.sort()
            lis = []
            flag = False
            count = 0
            for i in range(len(A)):
                if flag == False:
                    for j in range(i+1,len(A)):
                        if xxx(A[i],A[j]):
                            lis.append(A[i])
                            lis.append(A[j])
                            A.remove(A[j])
                            A.remove(A[i])  
                            flag = True
                            break
            while len(A) > 1 and count <= n and lis:       
                for i in A:
                    flag = False
                    for j in range(len(lis)):
                        if flag == False:
                            x,y = i,lis[j]
                            if xxx(x,y):
                                lis.append(x)
                                A.remove(x)
                                flag = True
                if len(A) == 1:
                    for i in range(len(lis)):
                        if xxx(lis[i],A[0]):
                            lis.append(A[0])
                            break
                count += 1
            print(lis)
            print(len(lis) == 6)
        except Exception as e:
            print(e.args)
            break
