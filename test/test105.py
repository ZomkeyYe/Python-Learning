# 提取不重复整数
if __name__ == '__main__':
    while True:
        try:
            x = input()
            xx = list(x)
            xx1 = set(x)
            xx2 = list(x)
            for i in xx1:
                if i in xx:
                    xx.remove(i)
            for j in xx:
                if j in xx2:
                    xx2.remove(j)
            print("".join(xx2[::-1]))
        except:
            break