# 统计字符
def zzz(str):
    x = list(set(str))
    x.sort()
    values = {}
    for i in x:
        values[i] = str.count(i)
    for i,j in values.items():
        print("{0}:{1}".format(i,j))
if __name__ == '__main__':
    N = input()
    zzz(N)
   