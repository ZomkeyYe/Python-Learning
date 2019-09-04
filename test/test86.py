# 成绩问题
if __name__ == '__main__':
    lll = list(map(int,input().split()))
    N = lll[0]
    lis = lll[1:N+1]  
    K = lll[N+1]
    lili = lll[-K:]
    xixi = []  
    for i in lili: 
        count = 0      
        for j in range(len(lis)):         
            if lis[j] == i:
                count +=1
        xixi.append(str(count))
    print(" ".join(xixi))