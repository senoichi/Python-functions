from string import maketrans

def encry (str):  

    #rot13 encryption
    intab = "BEHL"
    outtab = "ORUY"
    trantab = maketrans(intab, outtab)
    encryStr = str.translate(trantab, 'xm')
    
    return encryStr

print (encry('Hello World!, my name is Tony. How are you doing?'))