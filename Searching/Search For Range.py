# O(log(n)) time | O(1) space
def searchForRange(array, target):
	final = [-1, -1]
	binarySearch(array, target, 0, len(array) - 1, final, True)
	binarySearch(array, target, 0, len(array) - 1, final, False)
	return final

def binarySearch(array, target, left, right, final, exploreLeft):
	while left <= right:
		middle = (left + right) // 2
		middleNum = array[middle]
		if target > middleNum:
			left = middle + 1
		elif target < middleNum:
			right = middle - 1
		else:
			if exploreLeft:
				if middle == 0 or array[middle - 1] != target:
					final[0] = middle
					return
				else:
					right = middle - 1
			else:
				if middle == len(array) - 1 or array[middle + 1] != target:
					final[1] = middle
					return
				else:
					left = middle + 1

print(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))