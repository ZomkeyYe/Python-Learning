def numgame(x):
    count = 0
    for i in range(1,x+1):
        k = str(i)       
        m = list(k)   
        flag = False    
        for j in m:
            if j == '2' or j == '5' or j == '6' or j == '9':
                flag = True
        if flag == True:
            count += 1
    return count
if __name__ == '__main__':
    x = int(input())    
    print(numgame(x))