#华为机考第二题  判断输入序列是不是矩阵中的成员
def findRoot(x):
    if Tree[x] == -1:
        return x
    temp = int(findRoot(Tree[x]))
    Tree[x] = temp
    return temp
if __name__ == '__main__':
    A = []
    Tree = []
    while True:
        A = list(map(int,input().split()))
        for i in range(6):
            Tree.append(-1)
        for i in range(6):
            for j in range(i+1,6):
                x = max(A[i],A[j])
                y = min(A[i],A[j])
                if (x - y == 1) or (x - y == 10):
                    a = findRoot(i)
                    b = findRoot(j)
                    if a != b:
                        Tree[a] = b
        count = Tree.count(-1)
        print(Tree)
        if  count == 1:
            ans = 1
        else:
            ans = 0
        print(ans)
        Tree = []
