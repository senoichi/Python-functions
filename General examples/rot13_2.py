def encry (str):  
    
    key = {
            'A' : 'N',
            'B' : 'O',
            'C' : 'P',
            'D' : 'Q',
            'E' : 'R',
            'F' : 'S',
            'G' : 'T',
            'H' : 'U',
            'I' : 'V',
            'J' : 'W',
            'K' : 'X',
            'L' : 'Y',
            'M' : 'Z',
            'N' : 'A',
            'O' : 'B',
            'P' : 'C',
            'Q' : 'D',
            'R' : 'E',
            'S' : 'F',
            'T' : 'G',
            'U' : 'H',
            'V' : 'I',
            'W' : 'J',
            'X' : 'K',
            'Y' : 'L',
            'Z' : 'M',
            'a' : 'n',
            'b' : 'o',
            'c' : 'p',
            'd' : 'q',
            'e' : 'r',
            'f' : 's',
            'g' : 't',
            'h' : 'u',
            'i' : 'v',
            'j' : 'w',
            'k' : 'x',
            'l' : 'y',
            'm' : 'z',
            'n' : 'a',
            'o' : 'b',
            'p' : 'c',
            'q' : 'd',
            'r' : 'e',
            's' : 'f',
            't' : 'g',
            'u' : 'h',
            'v' : 'i',
            'w' : 'j',
            'x' : 'k',
            'y' : 'l',
            'z' : 'm'
            }
    #rot13 encryption
    cypher = [] 
    for char in str:
        if char in key:
            cypher.append(key[char])
        else:
            cypher.append(char)
    return ''.join(cypher)

print ('Hello World!, my name is Tony. How are you doing?')
print (encry('Hello World!, my name is Tony. How are you doing?'))

