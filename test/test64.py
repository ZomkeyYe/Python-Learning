# 安置路灯
def zomkey(str1,k):
    light = 0
    count = 0
    while count < k:
        if str1[count]=='.':
            light += 1
            count += 3
        else:
            count += 1;
    return light
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        k = int(input())
        str1 = input()
        print(zomkey(str1,k))