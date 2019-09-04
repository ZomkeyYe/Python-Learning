# 数字黑洞
def zom(N):
    N1 = sorted(N,reverse=True)
    N1 = "".join(N1)
    N2 = sorted(N)
    N2 = "".join(N2)
    N3 = str(int(N1)-int(N2))
    print(N1.rjust(4,"0")+" - "+N2.rjust(4,"0")+" = "+N3.rjust(4,"0"))
    return N3
if __name__ == '__main__':
    N = input()
    if N == "6174":
        print('7641 - 1467 = 6174')
    while N != "6174":
        N = zom(N.rjust(4,"0"))
        
