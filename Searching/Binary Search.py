# O(log(n)) time | O(1) space 
def binarySearch(array, target):
	left = 0
	right = len(array) - 1
	while left <= right:
		middle = (left + right)//2
		if target == array[middle]:
			return middle
		elif target < array[middle]:
			right = middle - 1
		else:
			left = middle + 1
	return -1

print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 71))