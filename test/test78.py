# A/B
def zzz(a,b):
    Q = a//b
    R = a%b
    return Q,R
if __name__ == '__main__':
    a,b = map(int,input().split())
    x,y = zzz(a,b)
    print(x,y)