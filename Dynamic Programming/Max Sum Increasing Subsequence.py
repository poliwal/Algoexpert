# O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
	sums = array[:]
	sequences = [None for _ in array]
	maxSumIdx = 0
	for i in range(len(array)):
		currentNum = array[i]
		for j in range(i):
			previousNum = array[j]
			if previousNum < currentNum and currentNum + sums[j] > sums[i]:
				sums[i] = currentNum + sums[j]
				sequences[i] = j
		if sums[i] > sums[maxSumIdx]:
			maxSumIdx = i
	return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]

def buildSequence(array, sequences, currentIdx):
	sequence = []
	while currentIdx is not None:
		sequence.append(array[currentIdx])
		currentIdx = sequences[currentIdx]
	return sequence[::-1]



print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))