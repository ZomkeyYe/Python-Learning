# 空汽水瓶
def main(n):
    if n == 1:
        return 0
    flag = n//3
    count = flag
    remain = n%3
    noo = flag + remain
    while flag >0:
        flag = noo//3
        remain = noo%3
        count += flag
        noo = remain + flag
    if noo ==2:
        count += 1
    return count
if __name__ == '__main__':
    lis = []
    while True:
        try:
            n = int(input())
            if n != 0:
                lis.append(main(n))
        except:
            break
    for i in lis:
        print(i)