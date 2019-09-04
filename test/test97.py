# 排序问题
def xxx(lis):
    a = list(set(lis))
    a.sort()
    return a
if __name__ == '__main__':
    
    while True:
        try:    
            N = int(input())
            lis = []   
            for i in range(N):
                lis.append(int(input()))
            x = xxx(lis)
            for i in x:
                print(i)
        except:
            break
    