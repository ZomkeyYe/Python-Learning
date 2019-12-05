if __name__ == "__main__":
    english = 0
    number = 0
    space = 0
    other = 0
    input_str = input()
    for i in input_str:
        if i == ' ':
            space += 1
        elif (i >= 'a'and i <= 'z') or (i >='A' and i <='Z') :
            english += 1
        elif i in '0123456789':
            number += 1
        else:
            other += 1
    print("输入的字符串中，英文字母有%d个，空格有%d个，数字有%d个，其它字符有%d个"%(english,space,number,other))