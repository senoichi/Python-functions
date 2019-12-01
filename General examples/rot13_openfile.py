from string import maketrans

def encry (filename):  
	
	# Read lines from file
	f = open("filename", "r")
	lines =  f. readline()
	f.close
	
	#Name of encrypted file
	newName = ‘encry_ ’ + filename

	#Create encrypted file
    f = open("newName, "w")
    #rot13 encryption
    intab = "BEHL"
    outtab = "ORUY"
    trantab = maketrans(intab, outtab)
    encryLines = lines.translate(trantab, 'xm')
    	
    	#write to file
    f.write(encryLines)
    f.close()

