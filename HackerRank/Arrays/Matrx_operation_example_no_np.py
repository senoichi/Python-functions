import math

queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
n = 5

from operator import add

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    #print(n)
    z =[0]*(n+1)
    for row in queries:
        if len(row) < 3:
            row = row + [0]*(3 - len(row))
            
        y = [0 for i in range(row[0])] + [row[2] for i in range(row[0],row[1]+1)] + [0 for i in range(row[1]+1,n+1)]
        #print(y)
        z = list(map(add, z, y) )
    return (max(z))

    
                    
#print (arr2)   
print (arrayManipulation(n, queries))
#arrayManipulation(n, queries)