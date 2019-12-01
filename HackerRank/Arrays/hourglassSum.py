import math
arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]

# Complete the hourglassSum function below.
def hourglassSum(arr):
    
    max_hg = -63
    sum = 0
    #Starting row for eeach hour glass
    for i in range(len(arr[:-2])) :
        #Starting point for each hour glass
        for j in range(len(arr[i][:-2])):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum  > max_hg:
                max_hg = sum
    return max_hg
    

print(hourglassSum(arr))    
    
    
    
    
    
    