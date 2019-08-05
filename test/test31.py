def nn(a,b):
    return max(a+b,a*b)
def nnn(a,b,c):
    return max(nn(nn(a,b),c),nn(a,nn(b,c)),nn(b,nn(a,c)))
if __name__ == "__main__":
    lis = list(map(int,input().split()))
    print(nnn(lis[0],lis[1],lis[2]))