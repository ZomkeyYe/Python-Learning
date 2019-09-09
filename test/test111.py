# 正确的密码
if __name__ == '__main__':
    while True:
        try:
            x = ''
            s = input()
            dic = {
                'abc':'2',
                'def':'3',
                'ghi':'4',
                'jkl':'5',
                'mno':'6',
                'pqrs':'7',
                'tuv':'8',
                'wxyz':'9'
            }
            for i in s:
                if i.isupper():
                    if i == 'Z':
                        x += 'a'
                    else:
                        x += chr(ord(i.lower())+1)
                if i.isdigit():
                    x += i
                if i.islower():
                    for j in dic.keys():
                        if i in j:
                            x += dic[j]
            print(x)
        except:
            break
    