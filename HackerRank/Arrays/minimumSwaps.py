import math

arr = [1, 3, 5, 2, 4, 6, 7]
arr2 = [2, 3, 4, 1, 5]

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    #no. of swaps
    count = 0
    p1 = 0
    p2 = 0
    for i in range(len(arr)):
        if arr[i] > i+1:
            p1 = arr[i]
            for j in range(i+1,len(arr)):
                if arr[j] == i+1:
                    p2 == arr[j]
                    #Swap
                    arr[i], arr[j] = p2, p1
                    count += 1
    return count
                    
print (arr2)   
print (minimumSwaps(arr2))