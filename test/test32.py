import itertools
def cnm(n,m,k):
    x = 'a'
    y = 'z'
    z = x*n+y*m
    xx = [''.join(j) for j in itertools.permutations(z, 4)]
    yy = set(xx)
    zz = list(yy)
    zz.sort()
    if zz[k-1]:
        print(zz[k-1])
    else:
        print(-1)
if __name__ == "__main__":       
    arr = list(map(int,input().split()))
    n,m,k = arr[0],arr[1],arr[2]
    cnm(n,m,k)
