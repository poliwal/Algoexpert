# O(n) time | O(1) space
def moveElementToEnd(array, elemToMove):
	i = 0
	j = len(array)-1
	while i<j:
		while i<j and array[j]==elemToMove:
			j -= 1
		if array[i]==elemToMove:
			array[i],array[j] = array[j],array[i]
		i += 1
	return array


	###Another Method
	# c = array.count(elemToMove)
	# array = [x for x in array if x!=elemToMove]
	# array.extend([elemToMove]*c)
	# return array



print(moveElementToEnd([2,1,2,2,2,3,4,2],2))