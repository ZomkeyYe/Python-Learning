# 字符串包含问题
def mmm(str1,str2):
    if (str1 in str2) or (str2 in str1):
        print(1)
    else:
        print(0)
if __name__ == "__main__":
    str1,str2 = input().split()
    mmm(str1,str2)