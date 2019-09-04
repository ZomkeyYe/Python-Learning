# 零钱问题
def xixi(arr):
    return (arr[0]*17*29+arr[1]*29+arr[2])
def didi(n):
    print(n)
    n1 = n//(17*29)
    n2 = n%(17*29)//29
    n3 = n%(17*29)%29
    return [n1,n2,n3]
if __name__ == '__main__':
    a = input()
    a1,a2 = a.split()
    a1 = list(map(int,a1.split(".")))
    a2 = list(map(int,a2.split(".")))
    x = didi(xixi(a2)-xixi(a1))

    x = [str(i) for i in x]
    strr = ".".join(x)
    print(strr)