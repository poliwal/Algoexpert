############################## Iterative ##############################
# O(n*2^n) time | O(n*2^n) space
def powerset(array):
	subsets = [[]]
	for elem in array:
		for i in range(len(subsets)):
			currentSubset = subsets[i]
			subsets.append(currentSubset + [elem])
	return subsets




############################## Recursive ##############################
# O(n*2^n) time | O(n*2^n) space
def powerset(array, idx = None):
	if idx == None:
		idx = len(array) - 1
	elif idx < 0:
		return [[]]
	elem = array[idx]
	subsets = powerset(array, idx - 1)
	for i in range(len(subsets)):
		currentSubset = subsets[i]
		subsets.append(currentSubset + [elem])
	return subsets	




print(powerset([1, 2, 3]))	