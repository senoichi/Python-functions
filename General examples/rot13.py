def encry (str):  
    
    #rot13 encryption
    ordLetter = set([65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
 89, 90] + [ 97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122])
    newStr = []
    
    for char in str:
        if ord(char) in ordLetter :
            if ord(char) <= 77:
                enco = ord(char) + 13
                newStr.append(chr(enco))
                
            elif 77 < ord(char) < 91 :
                enco = ord(char) - 13
                newStr.append(chr(enco))
                
            elif  ord(char) <= 109 :
                enco = ord(char) + 13
                newStr.append(chr(enco))
                
            elif 109 < ord(char) < 123 :
                enco = ord(char) - 13
                newStr.append(chr(enco))
        else:
            newStr.append(char)
    
    return ''.join(newStr)
#print ('Hello World!, my name is Tony. How are you doing?')
print (encry('BIOS'))

