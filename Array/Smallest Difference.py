#O(nlogn + mlogm) time ;where n=len(arrayOne) and m=len(arrayTwo) | O(1) space
def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	a = 0   #points to arrayOne
	b = 0	#points to arrayTwo
	minDiff = float('inf')
	result = []
	while (a < len(arrayOne)) and (b < len(arrayTwo)):
		diff = abs(arrayOne[a] - arrayTwo[b])
		if diff < minDiff:
			minDiff = diff
			result = [arrayOne[a], arrayTwo[b]]
			if diff == 0:
				return result
		if arrayOne[a] < arrayTwo[b]:
			a += 1
		elif arrayOne[a] > arrayTwo[b]:
			b += 1
	return result

print(smallestDifference([-1,5,10,20,28,3], [26,134,135,15,17]))
