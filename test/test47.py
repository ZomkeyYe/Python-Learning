# 计算字符串中的回文子串
s=input()
n=len(s)
numbers=0
for i in range(n):
    for j in range(i+1,n+1):
        string=s[i:j]
        if string==string[::-1]:
            numbers+=1
print(numbers)