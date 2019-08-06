# 99乘法表
class nnn():
   def mmm(self):
      for i in range(1,10):
         for j in range(1,i+1):
            n=i*j
            print('{0}x{1}={2}'.format(i,j,n),end=''+' ')
         print()
if __name__ == "__main__":
   x=nnn()
   x.mmm()