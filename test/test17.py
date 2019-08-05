import re
str = '<div calss="nam">xixi</div>'
res=re.findall(r'<div calss=".*">(.*?)</div>',str)
print(res)