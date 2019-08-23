# 字符串加法
def zomkey(a,b):
    c = str(bin(a+b))
    d = c[2::]
    return d
def soo(lis):
    count = len(lis)-1
    sum = 0
    for i in lis:
        k = int(i)
        sum += k*2**(count)
        count -= 1
    return sum
if __name__ == '__main__':
    lis = input().split()
    a,b = lis[0],lis[1]
    a1,b1 = list(a),list(b)
    a,b = soo(a1),soo(b1)
    print(zomkey(a,b))


