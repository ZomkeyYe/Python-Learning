def cnm(str,str1,dic):
    count = 0
    for i in str1:
        if i in str:
            count+=dic[i]
    nnn = count%100
    mmm = count//100
    return [mmm,nnn]

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    str = "abcdefghijklmnopqrstuvwxyz"
    dic = {}
    for i in range(len(arr)):
        dic.update({str[i]:arr[i]})
    str1 =input()
    n,m=cnm(str,str1,dic)
    print(n,m)

