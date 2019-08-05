import sys
class StrCount:
    def start():
        str1 = input("本程序将统计字符串中各字符出现次数，请输入字符串：")        
        temp = list(str1)
        temp.sort()
        str1 = "".join(temp)
        print(str1)
        while len(str1)>0:
            first= str1[0]
            str2 = str1.replace(first,"")
            count = len(str1)-len(str2)
            if first==" ":
                first="空格"
            print("字符==>\t"+first+"\t出现了 "+str(count)+" 次！\n")
            str1 = str2 
if __name__ == "__main__":
    S = StrCount
    S.start()                
