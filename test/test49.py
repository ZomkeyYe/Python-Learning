# 加减法运算
s = input()
res = []

sign = 1
carr = 0
for ss in s:
    if ss == "-":         
        res.append(carr*sign)
        carr = 0
        sign = -1
        
    elif ss.isdigit():
        carr = carr*10 + int(ss)        
    else:
         
        res.append(carr*sign)
        carr = 0
        sign = 1

res.append(carr*sign)
print(sum(res))