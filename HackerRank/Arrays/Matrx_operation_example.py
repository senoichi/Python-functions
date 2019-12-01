import math

queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
n =10

import numpy as np
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    z = np.zeros(n)
    for row in queries:
        y = np.concatenate( [np.zeros((row[0])) , np.tile((row[2]),(row[1]-row[0]+1))])
        y = np.concatenate([y,np.zeros(int(n-row[1]-1))])
        z = z + y
    return (int(np.amax(z)))
    
                    
#print (arr2)   
print (arrayManipulation(n, queries))
#arrayManipulation(n, queries)