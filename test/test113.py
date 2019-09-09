# 删除字符串中出现次数最少的字符
if __name__ == '__main__':
    while True:
        try:
            s = input()
            minconut = len(s)
            for i in set(s):
                if s.count(i) < minconut:
                    minconut = s.count(i)
            for i in set(s):
                if s.count(i) == minconut:
                    s = s.replace(i,'')
            print(s)
        except:
            break