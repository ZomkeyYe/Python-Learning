import sys 
A = [64, 34, 25, 12, 22, 11, 90]
  
for i in range(len(A)): 
    print(A)   
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
                
    A[i], A[min_idx] = A[min_idx], A[i] 
print(A)