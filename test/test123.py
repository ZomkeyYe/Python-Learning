def party(lis):
    if lis[2] >= (lis[0]+lis[1])*2:
        return lis[0]+lis[1]
    else:
        return sum(lis)//3
if __name__ == '__main__':
    while True:
        try:
            T = int(input())
            for i in range(T):
                lis = list(map(int,input().split()))
                lis.sort()
                print(party(lis))
        except:
            break