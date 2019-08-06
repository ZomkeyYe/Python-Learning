# 最少数量货物装箱
def nnn(x):
    count_1 = 0
    count_2 = 0
    count_3 = 0
    m1 = x%7
    count_1 += x//7
    m2 =m1%5 
    count_1 += m1//5
    m3 =m2%3
    count_1 += m2//3

    n1 =x%5 
    count_2 += x//5
    n2 =n1%3
    count_2 += n1//3


    l1 =x%3
    count_3 += x//3


    if m3==0 and n2==0 and l1==0:
        return min(count_1,count_2,count_3)
    if (m3==0 and n2==0):
        return min(count_1,count_2)
    if (n2==0 and l1==0):
        return min(count_2,count_3)
    if (m3==0 and l1==0):
        return min(count_1,count_3)
    if m3==0:
        return count_1
    if n2==0:
        return count_2
    if l1==0:
        return count_3
    else:
        return -1

if __name__ == "__main__":
    x = int(input())
    print(nnn(x))