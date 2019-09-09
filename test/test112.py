s = "Li Yi Qiong I Love You"
for char in s.split():
   lis = []
   for y in range(12, -12, -1):
       arr = []
       dd = ''
       for x in range(-50, 50):
            f = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if f <= 0:
                dd += char[(x) % len(char)]
            else:
                dd += ' '
       arr.append(dd)
       lis += arr
   print('\n'.join(lis))
