# O(b + s) time | O(b + s) space
def smallestSubstringContaining(bigString, smallString):
	targetCharCounts = getCharCounts(smallString)
	substringBounds = getSubstringBounds(bigString, targetCharCounts)
	return getStringsFromBounds(bigString, substringBounds)

def getSubstringBounds(string, targetCharCounts):
	substringBounds = [0, float("inf")]
	leftIdx = 0
	rightIdx = 0
	substringCharCounts = {}
	numUniqueCharCount = len(targetCharCounts.keys())
	numUniqueCharCountDone = 0
	while rightIdx < len(string):
		rightChar = string[rightIdx]
		if rightChar not in targetCharCounts:
			rightIdx += 1
			continue
		increaseCharCounts(rightChar, substringCharCounts)
		if substringCharCounts[rightChar] == targetCharCounts[rightChar]:
			numUniqueCharCountDone += 1
		while numUniqueCharCount == numUniqueCharCountDone and leftIdx <= rightIdx:
			substringBounds = getSmallerBounds(leftIdx, rightIdx, substringBounds[0], substringBounds[1])
			leftChar = string[leftIdx]
			if leftChar not in targetCharCounts:
				leftIdx += 1
				continue
			if substringCharCounts[leftChar] == targetCharCounts[leftChar]:
				numUniqueCharCountDone -= 1
			decreaseCharCounts(leftChar, substringCharCounts)
			leftIdx += 1
		rightIdx += 1
	return substringBounds

def getStringsFromBounds(string, substringBounds):
	start, end = substringBounds
	if end == float("inf"):
		return ""
	return string[start: end + 1]

def getSmallerBounds(idx1, idx2, idx3, idx4):
	return [idx1, idx2] if idx2 - idx1 < idx4 - idx3 else [idx3, idx4]

def getCharCounts(string):
	charCounts = {}
	for char in string:
		increaseCharCounts(char, charCounts)
	return charCounts

def increaseCharCounts(char, charCounts):
	if char not in charCounts:
		charCounts[char] = 0
	charCounts[char] += 1

def decreaseCharCounts(char, charCounts):
	charCounts[char] -= 1





print(smallestSubstringContaining('abcd$ef$axb$c$', '$$abf'))