def mmm(str1):
    str2 = str1[-6::1]
    return(str2.sort())
if __name__ == "__main__":
    M = int(input())
    lis = []
    for i in range(M):
        str1 = input()
        lis.append(str1[-6:])
    lis.sort()
    for i in lis:
        print(i)