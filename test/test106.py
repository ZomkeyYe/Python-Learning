if __name__ == '__main__':
    while True:
        try:
            lis = [0,0]
            s = input().split(";")
            for i in s: 
                if i:           
                    if i[0] == 'A':
                        try:
                            lis[0] -= int(i[1:])
                        except:
                            continue
                    elif i[0] == 'S':
                        try:
                            lis[1] -= int(i[1:])
                        except:
                            continue
                    elif i[0] == 'W':
                        try:
                            lis[1] += int(i[1:])
                        except:
                            continue
                    elif i[0] == 'D':
                        try:
                            lis[0] += int(i[1:])
                        except:
                            continue
                    else:
                        continue
            lis = list(map(str,lis))
            print(",".join(lis))
        except:
            break