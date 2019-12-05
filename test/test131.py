'''
5 3
1 2 3 4 5
6
5 3
-2 1 -1 -1 -1
-4
'''
def xxx(minx,x):
    if x + 1 < len(A):
        if A[x+1] < 0:
            minx += A[x+1]
            return xxx(minx,x+1)
        else:
            return minx
    else:
        return minx
if __name__ == '__main__':
    while True:
        try:    
            n,m = map(int,input().split())
            A = list(map(int,input().split()))
            minx = sum(A[:m])
            for i in range(1,len(A)-m+1):
                x = xxx(sum(A[i:i+m]),i+m-2)
                if x < minx:
                    minx = x
            print(minx)
        except:
            break