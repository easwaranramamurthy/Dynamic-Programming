def getSeqs():
	"""Function to get input sequences"""
	s1 = raw_input("Enter sequence 1: ")
	s2 = raw_input("Enter sequence 2: ")
	
	return s1, s2
	
def calcOpt(s1, s2, gap, mismatch, match):
	"""Calculates dynamic programming matrix"""
	#initialize 2d list with all zeros
	optMatrix = make2dList(len(s1)+1, len(s2)+1)
	rows = len(s1)+1
	cols = len(s2)+1
	
	#base case 1
	for i in xrange(0, rows):
		optMatrix[i][0] = gap*i
	#base case 2	
	for j in xrange(0, cols):
		optMatrix[0][j] = gap*j
	
	#recursive case
	for i in xrange(1, rows):
		for j in xrange(1, cols):
			optMatrix[i][j] = min(optMatrix[i-1][j-1] + cost(s1[i-1], s2[j-1], mismatch, match),
				gap+optMatrix[i-1][j], gap+optMatrix[i][j-1])
	
	return optMatrix
	
def cost(a, b, mismatch, match):
	"""Returns cost of aligning a with b"""
	if(a==b):
		return match
	
	return mismatch
	
def make2dList(rows, cols):
	"""Creates 2d list of zeros of dimension rows x cols"""
	a=[]
	for row in xrange(rows): a += [[0]*cols]
	return a

def maxItemLength(a):
	"""Helper function for print2dList"""
	maxLen = 0
	rows = len(a)
	cols = len(a[0])
	for row in xrange(rows):
		for col in xrange(cols):
			maxLen = max(maxLen, len(str(a[row][col])))
	return maxLen

def print2dList(a):
	"""Prints 2d lists in a better way"""
	if (a == []):
		# So we don't crash accessing a[0]
		print []
		return
	rows = len(a)
	cols = len(a[0])
	fieldWidth = maxItemLength(a)
	print "[ ",
	for row in xrange(rows):
		if (row > 0): print "\n  ",
		print "[ ",
		for col in xrange(cols):
			if (col > 0): print ",",
			# The next 2 lines print a[row][col] with the given fieldWidth
			format = "%" + str(fieldWidth) + "s"
			print format % str(a[row][col]),
		print "]",
	print "]"	

def traceBack(opt, s1, s2, gap, mismatch, match):
	"""Function to trace back on the opt matrix to find optimal alignment"""
	rows = len(opt)
	cols = len(opt[0])
	
	#initializes two empty strings for building alignment strings
	al1=""
	al2=""
	#start at last element
	row = rows-1
	col = cols-1
	while(row!=0 and col!=0):
		#if match or mismatch is favorable
		if(opt[row][col] == cost(s1[row-1], s2[col-1], mismatch, match) + opt[row-1][col-1]):
			al1=s1[row-1]+al1
			al2=s2[col-1]+al2
			row-=1
			col-=1	
		#if aligning gap with sequence 1 is favorable	
		elif(opt[row][col] == gap+opt[row-1][col]):
			al1=s1[row-1]+al1
			al2="_"+al2
			row-=1
		#if aligning gap with sequence 2 is favorable	
		elif(opt[row][col] == gap+opt[row][col-1]):
			al1="_"+al1
			al2=s2[col-1]+al2
			col-=1
	
	return al1, al2
	
def printAlignment(al1, al2):
	"""Function to print alignment in acceptable format. (X-mismatch, |-match)"""
	print "\nThe optimal alignment is:"
	for ch in al1:
		print ch,
	print
	for i in xrange(len(al1)):
		if(al1[i]==al2[i]):
			print "|",
		elif(al1[i]!="_" and al2[i]!="_"):
			print "X",
		else:
			print " ",
	print		
	for ch in al2:
		print ch,

def getParams():
	"""To get alignment scoring parameters from user"""
	gap = int(raw_input("Enter gap penalty: "))
	mismatch = int(raw_input("Enter mismatch penalty: "))
	match = int(raw_input("Enter match score: "))
	return gap, mismatch, match
	
if __name__=="__main__":
	#get input sequences
	s1, s2 = getSeqs()
	
	#get parameters
	gap, mismatch, match = getParams()
	
	#calculate optimal edit distance matrix using dynamic programming recursion
	optMatrix = calcOpt(s1, s2, gap, mismatch, match)
	
	#prints the scoring matrix
	print "\nOpt matrix:"
	print2dList(optMatrix)
	
	#builds alignment strings via traceback
	al1, al2 = traceBack(optMatrix, s1, s2, gap, mismatch, match)
	
	#prints alignment in acceptable format
	printAlignment(al1, al2)