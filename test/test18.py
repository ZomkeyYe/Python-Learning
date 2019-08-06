# 正则表达式
import re
a = "not 404 found 张三 99 深圳"
l1 = a.split (" ")
print(l1)  
res = re.findall('\d+|[a-zA-Z]+',a)
for i in res:
    if i in l1:
        l1.remove(i)
new_str = " ".join(l1)
print(res)
print(new_str)  