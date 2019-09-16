# bigmother
s = "#"
lis = [32,30,33,34]
month = ['June','July','August','September']
res = [([' ']*50) for i in range(11)]
count = 0
for x in lis:
    count += 10
    sy = ' '
    cc = 0
    for y in range(count-5,count):
        res[-(x-24)-1][y] = sy    
        if sy == ' ' and cc == 0:
            sy = str(list(str(x))[0])
            cc += 1
            continue
        if sy == str(list(str(x))[0]) and cc == 1:
            sy = str(list(str(x))[1])   
            cc += 1  
            continue
        if sy == str(list(str(x))[1]) and cc == 2:
            sy = ' '
            continue
    for xx in range(-(x-24),0,1):
        for xxx in range(count-5,count):
            res[xx][xxx] = s
for i in range(5):
    print("\n")
title = '               大姨妈周期(天)'
print(title)
for i in range(len(res)):    
    res[i] = "".join(res[i])
    print(res[i])

print("     "+month[0]+"      "+month[1]+"     "+month[2]+"   "+month[3])
