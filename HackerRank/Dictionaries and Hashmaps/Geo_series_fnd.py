import numpy as np
arr1 = np.tile([1],100)
arr = [1, 3, 9, 9, 27, 81,81]
r = 3
def op2(y):
        arr = [1,2,3,5,7,9,9]
        set(arr).discard(y)
        arr = list(set(arr))
        return arr
# Complete the freqQuery function below.
def freqQuery(queries):
    out = []
    ar = []
    def op1(arr,x):
            arr.append(x)
            return arr
    def op2(arr,y):
        a = set(arr).discard(y)
        return  list(set(a))
    def op3(arr,z):
        cont = 1
        a = sorted(arr[:-1])
        for i in range(len(a)):
            if a[i] == a[i+1]:
                cont += 1
            elif cont == z:
                return 1
            
        return 0
    
    for op in queries:
        if op[0] == 1:
            ar = op1(ar,op[1])
        elif op[0] == 2:
            ar = op2(ar,op[1])
        elif op[0] == 3:
            out.append(op3(ar,op[1]))
    return out
            





print(queries)
print(freqQuery)       