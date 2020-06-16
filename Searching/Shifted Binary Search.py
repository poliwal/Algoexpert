# O(log(n)) time | O(1) space
def shiftedBinarySearch(array, target):
	left = 0
	right = len(array) - 1
	while left <= right:
		middle = (left + right) // 2
		middleNum = array[middle]

		if middleNum == target:
			return middle

		leftNum = array[left]
		rightNum = array[right]
		if leftNum <= middleNum:
			if target < middleNum and target >= leftNum:
				right = middle - 1
			else:
				left = middle + 1
		else:
			if target > middleNum and target <= rightNum:
				left = middle + 1
			else:
				right = middle - 1
	return -1


print(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 33))