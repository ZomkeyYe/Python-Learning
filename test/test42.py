# 字符串a-z计数
class StrCount:
    def start():
        str1 = input()        
        temp = list(str1)
        temp.sort()
        str1 = "".join(temp)
        x = ''
        while len(str1)>0:
            first= str1[0]
            str2 = str1.replace(first,"")
            count = len(str1)-len(str2)
            x+=first
            x+=str(count)            
            str1 = str2 
        print(x)
if __name__ == "__main__":
    S = StrCount
    S.start()                

