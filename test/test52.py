# 统计输入的字符串中字符的出现次数
def xxx(str):
    str1 = list(set(str))
    str1.sort()
    for i in str1:
        x = str.count(i)
        print("字符：{0} 出现了 {1} 次！".format(i,x))
if __name__ == "__main__":
    str = input()
    xxx(str)