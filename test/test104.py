# 合并记录
if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            dic = {}
            for i in range(N):
                lis = list(map(int,input().split()))
                if lis[0] in dic:
                    dic[lis[0]] += lis[1]
                else:
                    dic[lis[0]] = lis[1]
            for k,v in dic.items():
                print(k,v)
        except:
            break
