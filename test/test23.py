a=[1, 3, 6, 9, 7, 3, 4, 6]
a.sort()
print("从小到大排序：",a)
a.sort(reverse=True)
print("从大到小排序：",a)
b=list(set(a))
print("去重：",b)

