def maxSubArraySum(a):
	maxSoFar = 0
	maxEndingHere = 0
	finalIndex=0
	for i in xrange(len(a)):
		maxEndingHere = maxEndingHere + a[i]
		if(maxEndingHere<0):
			maxEndingHere = 0
		if(maxSoFar < maxEndingHere):
			maxSoFar = maxEndingHere
			finalIndex = i
	return maxSoFar, finalIndex
	
def findMaxSumElements(a, maxSum, finalIndex):
	if finalIndex==0:
		return [], 0
	
	index = finalIndex
	sum = maxSum
	while(sum!=0):
		sum = sum - a[index]
		index-=1
	
	firstIndex = index+1	
	values = a[firstIndex:finalIndex+1]
	return  values, firstIndex
	

def getDiagonals(a):
	rows = len(a)
	cols = len(a[0])
	diagonals = []
	for diagNo in xrange(rows+cols-1):
		diag = []
		for row in xrange(max(0,rows-diagNo-1), min(rows, rows-diagNo+cols-1)):
			col = row+diagNo-rows+1
			diag.append(a[row][col])
		diagonals.append(diag)
		
	return diagonals
	
if __name__=="__main__":
	inputMatrix = [[-4, 1, 8, 5, -2, -7, -6, -7, -8, -2], 
					[3, -5, 2, -2, -1, -2, 9, -2, 2, -4],
					[6, -1, 8, 1, 10, -9, -9, -6, -4, 1],
					[10, -4, 2, -10, -4, 3, 8, -9, -2, -3],
					[7, 9, -2, 4, 3, -7, 5, 3, 1, 1],
					[3, 3, -3, 10, 5, 4, -6, -9, -1, 0]]

	diagonals = getDiagonals(inputMatrix)
	for diagonal in diagonals:
		print "The elements in this diagonal are ", diagonal
		maxSum, finalIndex = maxSubArraySum(diagonal)
		maxSumElements, firstIndex = findMaxSumElements(diagonal, maxSum, finalIndex)	
		print "Max Contiguous Sum is ", maxSum
		print "Max sum ends at index ", finalIndex		
		print "Max sum elements are ", maxSumElements
		print "Max sum starts at index ", firstIndex
		print
