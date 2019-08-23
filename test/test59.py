# 统计输入的字符串中字符的出现次数

def xxx(str,k):
    count_1 = 0
    str1 = list(set(str))
    # str1.sort(key=str.index)
    for i in str1:
        x = str.count(i)
        if x == 1:
            count_1+=1
            if count_1==k:
                # print(i)
                b = list(i)
                print(b)
            else:
                print("Myon~")

if __name__ == "__main__":
        lis = []
        lis = list(input().split())  
        print(lis)         
        k = int(lis[0])
        str = lis[1]            
        xxx(str,k)
        