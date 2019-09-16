# 赛马
def quicksort(lis):
    if len(lis) <= 1:
        return lis
    mid = len(lis)//2
    first = [i for i in lis if i < lis[mid]]
    middle = [i for i in lis if i == lis[mid]]
    last = [i for i in lis if i > lis[mid]]
    return quicksort(first)+middle+quicksort(last)
def saima(lis):
    while len(lis) >= 2:
        x = lis.pop(0)
        y = lis.pop()
        if x == y:
            return 'NO'
    return 'YES'
if __name__ == '__main__':
    while True:
        try:
            T = int(input())
            for i in range(T):
                n = input()
                lis = list(map(int,input().split()))
                lis = quicksort(lis)
                print(saima(lis))  
        except:
            break   