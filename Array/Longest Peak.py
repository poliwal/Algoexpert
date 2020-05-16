# O(n) time | O(1) space
def longestPeak(array):
	longestPeakLength = 0
	i = 1
	while i < len(array)-1:
		if array[i-1] < array[i] and array[i] > array[i+1]:

			left = i - 2
			while left >= 0 and array[left] < array[left+1]:
				left -= 1

			right = i + 2
			while right < len(array) and array[right] < array[right-1]:
				right += 1

			currentPeakLength = right - left - 1

			longestPeakLength = max(longestPeakLength, currentPeakLength)

			i = right

		else:
			i += 1

	return longestPeakLength


print(longestPeak([1,2,3,3,4,0,10,6,5,-1,-3,2,3]))