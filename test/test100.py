# 字符集合问题
def xxx(a):
    d = list(a)
    b = list(a)
    c = set(b)
    for i in c:
        b.remove(i)
    for i in b:
        for j in range(len(d)-1,-1,-1):
            if d[j] == i:
                d.pop(j)
                break
    xx = "".join(d)
    return xx
if __name__ == '__main__':
    while True:
        try:
            a = input()
            print(xxx(a))
        except:
            break