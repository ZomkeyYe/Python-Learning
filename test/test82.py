# 组个最小数
def zzz(b):
    lis = []
    for i in range(10):
        if b[i] != 0:
            lis.append(str(i)*int(b[i]))
    x = "".join(lis)
    x = sorted(x)
    start = len(x)
    while "0" in x:
        x.remove("0")
    end = len(x)
    for i in range(start-end):
        x.insert(1,"0")
    xxx = "".join(x)
    print(xxx)
if __name__ == '__main__':
    a = input().split()
    zzz(a)
