arr = [1, 3, 9, 9, 27, 81]
r = 3
# Complete the countTriplets function below.
def countTriplets(arr, r):
    a = sorted(arr)
    num = 0
    s = 0
    re = []
    for i in range(len(a)):
        if a[i] == 1:
            num += 1
            #print(i)
        elif a[i] % r == 0:
           num += 1
           
           #print(num)
        try:
            if a[i] != a[i+1] :
                re.append(num)
                num = 0
        except IndexError:
            re.append(num)
    
    for i in range(len(re[:-2])):
                s += re[i]*re[i+1]*re[i+2]
                
                
    return s
#                    
#print (arr2)   
print (countTriplets(arr, r))
#countTriplets(arr, r)