import random

def generateNewSet(size):
	"""For generation of a new input set of weights of with no. of elements = size"""
	newSet = []
	for i in xrange(size):
		# adds random integer weights between -3 and 3 inclusive into input set
		newSet.append(random.randint(-3, 3))
		
	return newSet

def calcOpt(inputSet, maxWeight):
	"""Function to build the opt array using the dynamic programming recurrence relation"""
	
	#declare opt array of size n x W initialized with zeros
	optArray = []
	for i in xrange(len(inputSet)):
		optArray += [[0]*(maxWeight+1)]
	
	n = len(inputSet)
	W = maxWeight
	
	#fills in opt array according to recursive definition of the problem
	for i in xrange(1,n):
		for j in xrange(1,W+1):
			Wi = inputSet[i]
			#checking index out of bounds
			if(j-Wi>0 and j-Wi<=W):
				#recurrence relation
				optArray[i][j] = max(Wi+optArray[i-1][j-Wi], optArray[i-1][j])
			else:
				optArray[i][j] = optArray[i-1][j]
				
	print "\nOpt Matrix:"
	#print the opt array
	print2dList(optArray)
			
	return optArray

def maxItemLength(a):
	"""helper function print2dList function"""
	maxLen = 0
	rows = len(a)
	cols = len(a[0])
	for row in xrange(rows):
		for col in xrange(cols):
			maxLen = max(maxLen, len(str(a[row][col])))
	return maxLen

def print2dList(a):
	"""Helper function to aesthetically print 2d arrays"""
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

def traceBack(optArray, inputSet):
	"""Trace back to find the elements that are part of the max subset"""
	
	
	i = len(optArray)-1
	j = len(optArray[0])-1
	includeList = []
	while(i>=0 and j>=0):
		#include ith element only when opt value above it is not equal
		if(optArray[i][j] != optArray[i-1][j]):
			if(inputSet[i]>0):
				includeList.append(inputSet[i])
			j -= inputSet[i]
		i -=1
	return includeList


def printSet(inputSet):
	"""Prints the input set"""
	print "Input Set of Weights:"
	for elem in inputSet:
		print elem,
	print

if __name__=="__main__":
	#input size n
	setSize = 10
	#maxWeight allowed in the bag W
	maxWeight = 15
	#new input set generated
	inputSet = generateNewSet(setSize)
	printSet(inputSet)
	#dynamic programming algorithm to construct opt array
	optArray = calcOpt(inputSet, maxWeight)
	#traceback to give weights to be included in final solution
	includeList = traceBack(optArray, inputSet)
	
	#print included objects
	print "\nIncluded Object weights: "
	for i in xrange(len(includeList)):
		print includeList[i],