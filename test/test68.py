# 字符串旋转
def zomkey(a,b):
    for i in range(len(a)):
        flag = False
        a1 = a[0:i+1]
        a2 = a[i+1:]
        a3 = a2 + a1
        if a3 == b:
            flag = True
            break
    if flag == True:
        print("true")
    else:
        print("false")
if __name__ == '__main__':
    lis = input().split(";")
    l1,l2 = lis[0],lis[1]
    zomkey(l1,l2)