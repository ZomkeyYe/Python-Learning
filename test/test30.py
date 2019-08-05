def nnn(arr,x):
   first = 0
   last = len(arr)-1
   while first<=last:    
      mid = (first+last)//2  
      if arr[mid]>x:
         if mid == 0:
            return mid + 1
            break
         if arr[mid-1]<x:
            return mid + 1
            break
         last = mid - 1
      elif arr[mid]<x:
         if arr[mid+1]>x:
            return mid + 2
            break
         first = mid + 1
      elif arr[mid]==x:
         return mid + 1
         break
if __name__ == "__main__":
   n = input()
   arr = list(map(int,input().split()))
   arr1 = [arr[0]]
   for i in range(1,len(arr)):
      arr1.append(arr[i]+arr1[i-1])
   m = input()
   ask = list(map(int,input().split()))
   for i in ask:
      print(nnn(arr1,i))