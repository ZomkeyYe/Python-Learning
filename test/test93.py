# 进制转换
def bin_To_int(a,x=2):
    b = list(map(int,a))
    n = len(b)-1
    i = 0
    sum = 0
    while n >= 0 and i < len(b):
        sum += b[i]*(x**n)
        n -= 1
        i += 1
    return sum
if __name__ == '__main__':
    s = "1011"
    print(bin_To_int(s))
    