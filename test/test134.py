if __name__ == '__main__':
    while True:
        try:
            lis = input()
            if '+' in lis:
                lis = lis.split('+')
                print (int(lis[0])+int(lis[1]))
            elif '-' in lis:
                lis = lis.split('-')
                print (int(lis[0])-int(lis[1]))
            elif '*' in lis:
                lis = lis.split('*')
                print (int(lis[0])*int(lis[1]))
            elif '/' in lis:
                lis = lis.split('/')
                print (int(lis[0])/int(lis[1]))
        except:
            break
    