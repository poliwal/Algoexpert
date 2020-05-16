#O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
	array.sort()
	result = []
	for i in range(len(array)-2):
		currElem = array[i]
		left = i+1
		right = len(array)-1
		while left < right:
			if currElem+array[left]+array[right] < targetSum:
				left += 1
			elif currElem+array[left]+array[right] > targetSum:
				right -= 1
			else:
				result.append([currElem,array[left],array[right]])
				left += 1
				right -= 1
	return result

print(threeNumberSum([12,3,1,2,-6,5,-8,6], 0))