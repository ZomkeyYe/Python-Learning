def xxx(arr,n):
   arr2=[]
   for i in range(n): 
      arr2.append(0)
   for i in arr:      
      for j in range(n):
         if i==(j+1):
            arr2[j]+=1
   return min(arr2)
   
if __name__ == "__main__":
   a = list(map(int,input().split()))
   n,m=a[0],a[1]
   arr = list(map(int,input().split()))
   print(xxx(arr,n))
         
