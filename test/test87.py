a = "genglengelnh33lny303nholn3lhn23ln2lhn320hgGBALNEBHLNBLNLNAGLLBNERLRNLBNRNLRNLASNBLASFNBGSH4HRJN544NBELNH40WNBLGaganlegnelg"
b = "3jtgeophnwe4ltnlbhewnhlrhnrlknr"
flag = True
lis = []
dd = set(b)
for i in dd:
    if i in a:       
        if a.count(i) < b.count(i):
            x = b.count(i)-a.count(i)
            lis.append(x)
            flag = False
    else:
        lis.append(b.count(i))
        flag = False
if flag == True:
    print("Yes"+" "+str(len(a)-len(b)))
else:
    print("No "+str(sum(lis)))