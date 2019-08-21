# 群发问题
def zomkey(name,group):
    group = group.split(",")
    if name in group:
        return group
    else:
        return 1
def zomkey1(group1,group2):
    flag = False
    for i in group1:
        if i in group2:
            flag = True
            return list(set(group1+group2))
            break
    if flag == False:
        return group1     
if __name__ == '__main__':
    name = input()
    N = int(input())
    count = []
    if N == 1:
        x = zomkey(name,input())
        if x != 1:
            print(len(x))
        else:
            print(x)
    else:
        for i in range(N):
            if i ==0:
                group = input()
                count += zomkey(name,group)
            else:
                group = input().split(",")
                count = list(set(zomkey1(count,group)+count))
        print(len(count))