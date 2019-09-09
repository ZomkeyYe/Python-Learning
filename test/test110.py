# 验证密码是否合格
if __name__ == '__main__':
    while True:    
        try:
            s = input()
            flag = True
            if len(s) <= 8:
                flag = False
            count = 0
            count_1 = False
            count_2 = False
            count_3 = False
            count_4 = False
            for i in s:
                if i.islower():
                    count_1 = True
                if i.isupper():
                    count_2 = True
                if i.isdigit():
                    count_3 = True
                elif (not i.islower()) and (not i.isupper()) and (not i.isdigit()):
                    count_4 = True
            for i in count_1,count_2,count_3,count_4:
                if i == True:
                    count += 1
            if count < 3:
                flag = False
            else:
                for i in range(len(s)):
                    for j in range(len(s)-1,i,-1):
                        if len(s[i:j]) > 2:
                            if s.count(s[i:j]) > 1:
                                flag = False
            if flag == True:
                print("OK")
            elif flag == False:
                print("NG")
        except:
            break
