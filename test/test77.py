def zom(str1,p):
    count = 0
    for i in str1:
        if i == p:
            count +=1
    return p*count
if __name__ == '__main__':
    str1,p1,str2,p2 = input().split()
    print(int(zom(str1,p1))+int(zom(str2,p2)))
