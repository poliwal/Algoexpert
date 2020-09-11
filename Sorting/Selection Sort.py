# O(n^2) time | O(1) space
def selectionSort(array):
	currentIdx = 0
	while currentIdx < len(array) - 1:
		smallesValueIdx = currentIdx
		for i in range(currentIdx + 1, len(array)):
			if array[smallesValueIdx] > array[i]:
				smallesValueIdx = i
		array[smallesValueIdx], array[currentIdx] = array[currentIdx], array[smallesValueIdx]
		currentIdx += 1
	return array


print(selectionSort([8, 5, 2, 9, 5, 6, 3]))