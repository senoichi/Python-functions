from collections import Counter

s0 = 'abba'
s1 = 'abcd'
s2 = 'ifailuhkqq'
s3 = 'kkkk'
s4 = 'abb'
def combin(n):
    return n*(n-1)/2
def sherlockAndAnagrams(s):
    count = 0
    subspace = set([s[0: j] for j in range(1,len(s))] + list(s)[1:])  

    for sub in subspace:
        blockSize = len(sub)
        numSub = 0
        print(f'substrings: {sub}')
        for i in range(len(s) - blockSize+1):
            if sum(bytearray(sub,'ascii')) == sum(bytearray(s[::-1][i:i+blockSize],'ascii')):
                
                numSub += 1
        if sub == sub[::-1]:
            print(f'block: {s[::-1][i:i+blockSize]}')
            count += combin(numSub)
        else:
            print(f'block: {s[::-1][i:i+blockSize]}')
            count += combin(numSub+1)
        #count += nonCon
        #print(sub,consec)
    return int(count), subspace

#print(s2[0:3],s2[0:3][::-1])
print(sherlockAndAnagrams(s2))
a = sum(bytearray('ifa','ascii'))
b = sum(bytearray('afi','ascii'))
c = a == b

#print(a,b,c)