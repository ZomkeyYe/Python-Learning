# 最长对称子字符串
def zomkey(str1):
    maxi = ''
    if len(str1) <= 1:
        return str1
    else:          
        for i in range(len(str1)):
            for j in range(len(str1)-1,i,-1):       
                strr = str1[i:j+1:] 
                if strr == strr[::-1]:
                    if len(maxi)<=len(strr):
                        maxi = strr
    return maxi
if __name__ == '__main__':
    str1 = input()
    print(zomkey(str1))