
arry = ['a','c','v','m']

#imput array, number of rtations and  direction (0 == left, 1 == right)
def rotate(arr,num,d):
    if d == 0:
        shift = num % len(arr)
        arry = arr[shift:] + arr[:shift]
        return arry
    elif d == 1:
        LS = len(arr) - (num % len(arr))
        RS = num % len(arr)
        arry = arr[::-1][:RS] + arr[:LS] 
        return arry

print(f'{arry}\n{rotate(arry,4,1)}')




