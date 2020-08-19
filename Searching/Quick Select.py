# O(n) time | O(1) space
def quickSelect(array, k):
	position = k - 1
	return quickSelectHelper(array, 0, len(array) - 1, position)

def quickSelectHelper(array, startIdx, endIdx, position):
	while True:
		if startIdx > endIdx:
			raise Exception("Should never arrive here.")
		pivotIdx = startIdx
		leftIdx = pivotIdx + 1
		rightIdx = endIdx
		while leftIdx <= rightIdx:
			if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
				swap(leftIdx, rightIdx, array)
			if array[leftIdx] <= array[pivotIdx]:
				leftIdx += 1
			if array[rightIdx] >= array[pivotIdx]:
				rightIdx -= 1
		swap(pivotIdx, rightIdx, array)
		if rightIdx == position:
			return array[rightIdx]
		elif rightIdx < position:
			startIdx = rightIdx + 1
		else:
			endIdx = rightIdx - 1

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
			 
	


print(quickSelect([8, 5, 2, 9, 7, 6, 3], 3))