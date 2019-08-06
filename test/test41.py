def zom(str1):
    dic = {0:'N',1:'E',2:'S',3:'W'}
    count = 0
    for i in range(len(str1)):
        if str1[i] == 'L':
            count-=1
        elif str1[i] == 'R':
            count+=1
    count=(count%4)
    return(dic[count])
if __name__ == "__main__":
    x = input()
    str1 = input()
    print(zom(str1))