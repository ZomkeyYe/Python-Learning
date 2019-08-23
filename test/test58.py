# 时间问题
import datetime
import time
year,month,day = map(int,(input().split()))
result = datetime.date(year, month,day)
x = result.strftime("%m")
print("d%"%x)