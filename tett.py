# 数字黑洞
def hd(l):
    l1=sorted(l,reverse=True)
    l1="".join(l1)
    # print(l1)
    l2=sorted(l,reverse=False)
    l2="".join(l2)
    # print(l2)
    l3=str(int(l1)-int(l2))
    print(l1.rjust(4,'0')+"-"+l2.rjust(4,'0')+"="+l3.rjust(4,'0'))
    return l3
if __name__ == "__main__":
    l=input()
    if l=="6174":
        print("7621-1267=6174")
    while l!="6174":
        l=hd(l).rjust(4,'0')