import math


# Complete the minimumBribes function below.
q = [2, 5, 1, 3, 4]
#q = [2, 1, 5, 3, 4] 
#q = sorted(range(5))

def minimumBribes(q,n=None):
    if n == None:
        n = len(q)
    count = 0

    # for i in range(len(q)):
    #     if q[i] > i + 3:
    #         print('Too chaotic')
    #         n = 1
    #         break

    for i in range(n-1):
        #print(i)
        if q == sorted(q):
            print(count)
            break
        elif q[i] > i + 3:
            print('Too chaotic')
            break
        elif q[i] > i+1:
            temp = q[i]
            q[i] = q[i+1]
            q[i+1] = temp
            count += 1
            if q[i+1] > i+2:
                temp = q[i+1]
                q[i+1] = q[i+2]
                q[i+2] = temp
                count += 1

minimumBribes(q)