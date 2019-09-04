# 画正方形
def zomkey(N,s): 
    print(s*N)  
    for i in range((N+1)//2-2):     
        print(s+' '*(N-2)+s)
    print(s*N)
            
if __name__ == '__main__':
    while True:
        try:
            lis = input().split()
            N,s = int(lis[0]),lis[1]
            if N//2 == 1:
                print(s*N)
                print(s*N)
                break
            zomkey(N,s) 
        except Exception:
            break
