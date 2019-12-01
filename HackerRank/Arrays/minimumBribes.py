import math

#q = [2, 5, 1, 3, 4]
q = [2, 1, 5, 3, 4]  

# Complete the minimumBribes function below.
def minimumBribes(arr):
    #no. of swaps
    #bribes = []
    count = 0
    p1 = 0
    p2 = 0
    i = 0
    num = len(arr)
    val = True
    while val :
        if num <= 1:
            val =False
        elif arr[i] != num:
            i += 1
            
        else:
            if arr[i] != i+1:
                p1 = arr[i]
                p2 = arr[i+1]
                #Swap
                arr[i], arr[i+1] = p2, p1
                count += 1                 
                if arr[i+1] != i+2:
                    p1 = arr[i+1]
                    p2 = arr[i+2]
                    #Swap
                    arr[i+1], arr[i+2] = p2, p1
                    count += 1
                    if arr[i+2] != i+3:
                        print('Too chaotic')
                        break
            i = 0
            num -= 1
    if val == False:
        print(count)
    
    
    
    
    
#    #no. of swaps
#    count = 0
#    p1 = 0
#    p2 = 0
#    for i in range(len(arr)):
#        if arr[i] > i+1:
#            p1 = arr[i]
#            p2 == arr[i+1]
#            #Swap
#            arr[i], arr[i+1] = p2, p1
#            count += 1
#            if arr[i] > i+1:
#                p1 = arr[i]
#                p2 == arr[i+1]
#                #Swap
#                arr[i], arr[i+1] = p2, p1
#                count += 1
#                if arr[i] > i+1:
#                    print( 'Too Chaotic')
#                    
#    print( count)

#print(q)
minimumBribes(q)