lis = [0,0]
s = "A10;S20;W10;D30;X;A1A;B10A11;;A10;".split(';')
for i in s: 
    if i:
        print(i)              
        if i[0] == 'A':
            try:
            # if int(i[1:]):
                lis[0] -= int(i[1:])
            except:
                continue
        elif i[0] == 'S':
            try:
            # if int(i[1:]):
                lis[1] -= int(i[1:])
            except:
                continue
        elif i[0] == 'W':
            try:
            # if int(i[1:]):
                lis[1] += int(i[1:])
            except:
                continue
        elif i[0] == 'D':
            try:
            # if int(i[1:]):
                lis[0] += int(i[1:])
            except:
                continue
        else:
            continue
print(lis)