# 查找数组中的众数
def zomkey(a):
    b = set(a)
    for i in b:
        count = 0
        for j in a:
            if i == j:
                count += 1
                if count > len(a)//2:
                    x = i
    print(x)
if __name__ == '__main__':
    lis = input()
    lis1 = lis[1:-1]   
    lis2 = list(map(int,lis1.split(",")))
    zomkey(lis2)