''' 华为机考第一题，三角形
主要通过i+j+k=l   i^2+j^2=k^2得出j = l-l^2/(2l-2i)
三重循环，二重循环都太复杂了，二重循环优化后（i<l/3，i<=j<l/3）'''
if __name__ == '__main__':
    while True:
        try:
            count = 0
            l = int(input())
            for i in range(1,l//3):
                j = l - float(l**2/(2*l-2*i))
                if (i<j) and (j-int(j) == 0):
                    count += 1
                    print(int(i),int(j),int(l-i-j))
            print(count)
        except:
            break