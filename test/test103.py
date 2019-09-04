# 四舍五入
if __name__ == '__main__':
    while True:
        try:
            s = input().split(".")
            if int(s[1]) >=5:
                print((int(s[0])+1))
            else:
                print(s[0])
        except:
            break