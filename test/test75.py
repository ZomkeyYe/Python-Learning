import math
def num(x):
    if x <= 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):#判断是否素数
        if x%i ==0:
            return False
    return True
if __name__ == '__main__':
    k,m = map(int,input().split()) 
    a = ["2"]
    start = 3
    while len(a) < m:       
        if num(start):
            a.append(str(start))
        start += 2
    for i in range(k-1,m,10):
            print(" ".join(a[i:i+10]))