sss = 'apple 最近 推出 了 新版 iPhone .'
print(sss)
for i in range(len(sss)):  
    if sss[i] == ' ':
        if (33<=ord(sss[i-1])<=47) or (33<=ord(sss[i+1])<= 47):
            sss = sss.replace(' ','*',1)
        elif (ord(sss[i-1])>= 256) and (ord(sss[i+1])>=256):
            sss = sss.replace(' ','*',1)
        else:
            sss = sss.replace(' ','+',1)
sss = sss.replace('*','')
sss = sss.replace('+',' ')
print(sss)