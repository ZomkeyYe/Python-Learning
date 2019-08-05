def numb(arr):
   arr.sort()
   res = []
   res.append(arr[0])
   for i in range(1,len(arr)):
      if(arr[i][0]>res[-1][1]):
         res.append(arr[i])
      else:
         res[-1][1] = max(res[-1][1],arr[i][1])
   for val in res:
      print(val[0],val[1])
if __name__ == "__main__":
   arr = []
   N = int(input())
   for i in range(N):
      arr.append(list(map(int, input().split(" "))))
   
   numb(arr)
      

