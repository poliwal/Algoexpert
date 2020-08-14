# O(n) time | O(1) space
def kadanesAlgorithm(array):
	maxSoFar = array[0]
	maxEndingHere = array[0]
	for num in array[1:]:
		maxEndingHere = max(maxEndingHere + num, num)
		maxSoFar = max(maxSoFar, maxEndingHere)
	return maxSoFar



print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))