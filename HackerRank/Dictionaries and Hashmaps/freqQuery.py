queries = [[3, 4], [2, 1003], [1, 16], [3, 1]]
#[(1,5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2)]


def op2(arr,y):
        for num in arr:
            if num == y:
                arr.remove(y)
                return arr


# Complete the freqQuery function below.
def freqQuery(queries):
    out = []
    ar = []
    def op1(arr,x):
            arr.append(x)
            return arr
    def op2(arr,y):
        if len(arr) == 0:
            return arr
        for num in arr:
            if num == y:
                arr.remove(y)
                return arr
    def op3(arr,z):
        cont = 1
        a = sorted(arr)
        if len(arr) == 1 and z == 1:
            return 1
        for i in range(len(a[:-1])):
            if a[i] == a[i+1]:
                cont += 1
                if cont == z:
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
#print(freqQuery(queries))
freqQuery(queries)
#print(op2([5, 6, 10, 10, 6],5))