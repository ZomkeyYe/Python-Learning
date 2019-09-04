# 输出固定长度字符串问题
def xxx(s):
    if len(s) < 8:
        s = s + '0'*(8-len(s))
        print(s)
    elif len(s) > 8:
        x = s[0:8]
        print(x)
        return xxx(s[8:])
    else:
        print(s)

if __name__ == '__main__':
    while True:
        try:
            lis = []
            s = input()
            xxx(s)

        except:
            break
    