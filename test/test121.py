# 画板
def huaban(lis): 
    return ((lis[2]-lis[0])+1)*((lis[3]-lis[1])+1)
if __name__ == '__main__':
    while True:
        try:
            T = int(input())
            for i in range(T):
                n = int(input())
                summ = 0
                for i in range(n):
                    lis = list(map(int,input().split()))
                    summ += huaban(lis)
                print(summ)
        except:
            break