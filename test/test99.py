# 删数问题
def xxx(n):
    lis = [i for i in range(n)]
    count = 1
    
    while len(lis) > 1:
        temp = []
        for i in range(len(lis)):
            if count%3 != 0:
                temp.append(lis[i])
            count += 1
        lis = temp
    return lis[0]
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(xxx(n))
        except:
            break