def jiec(n):
   if n ==1 :
      return 1
   return n*jiec(n-1)
print(jiec(5))