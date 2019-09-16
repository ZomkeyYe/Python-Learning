# 交易
def jiaoyi(lis):
    if sum(lis) == 0:
        return -1
    elif sum(lis)%len(lis) != 0:
        return -1
    else:
        return sum(lis)/len(lis)
if __name__ == '__main__':
    while True:
        try:
            T = int(input())
            for i in range(T):
                lis = list(map(int,input().split()))
                print("%d"%jiaoyi(lis))
        except:
            break
    