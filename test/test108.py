if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            dic = {}
            for i in range(N):
                arr = input().replace(" ","").split("=")
                dic[arr[0]] = arr[1]
            lis = [i for i in dic.keys()]
            listt = dic[lis[-1]].split("+")
            summ = 0
            for i in listt:
                if i.isdigit():
                    summ += int(i)
                else:    
                    if i in dic.keys():
                        if dic[i].isdigit():
                            summ += int(dic[i])
                        else:
                            if dic[i] in dic.keys():
                                summ += int(dic[dic[i]])
                            else:
                                print("NA")
                                summ = 0
                                break
                    else:
                        print("NA")
                        summ = 0
                        break
            if summ:
                print(summ)
        except:
            break