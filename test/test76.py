# 福尔摩斯的约会
def judge(str1,str2,str3,str4):  
    days = {
        'A':'MON',
        'B':'TUE',
        'C':'WED',
        'D':'THU',
        'E':'FRI',
        'F':'SAT',
        'G':'SUN'
    }
    for i in str1:
        if i in str2 and i in days:
            day = i
            start = str1.index(day)
            end = str2.index(day)
            break
    day = days[day]
    for i in str1[start+1:]:
        if i in str2[end+1:]:
            if 'A' <= i <= 'N' or i in "0123456789":
                hour = i
                break
    if hour in "0123456789":
        hour = int(hour)
    else:
        hour = ord(hour)-ord('A')+10
    for i in range(len(str3)):
        if str3[i] == str4[i]:
            if 'A'<= str3[i] <= 'Z' or 'a' <= str3[i] <= 'z':
                minute = i
                break
    return day,hour,minute
if __name__ == '__main__':
    str1 = input()
    str2 = input()
    str3 = input()
    str4 = input()
    day,hour,minute = judge(str1,str2,str3,str4)
    print("%s %02d:%02d" % (day, hour, minute))