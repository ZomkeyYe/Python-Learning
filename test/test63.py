# 数字序列第n位的值
def zomkey(k):
    for i in range(k):
        if i*(i+1)/2 < k:
            if (i+2)*(i+1)/2 >=k:
                return i+1
                break
if __name__ == '__main__':
    k = int(input())
    print(zomkey(k))  