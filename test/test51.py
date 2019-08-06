# 时间问题


import datetime
import time
year,month,day = map(int,(input().split()))
result = datetime.date(year, month,day)
if year == 1999 and month ==1 and day ==1:
    print(1)
else:
    print(result.strftime("%j"))