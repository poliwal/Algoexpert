# ############################### 1 ###############################
# # O(w*n*log(n)) time | O(wn) space   ;w is number of words, n is maximum length of word
def groupAnagrams(words):
	anagrams = {}
	for word in words:
		sortedWord = ''.join(sorted(word))
		if sortedWord in anagrams:
			anagrams[sortedWord].append(word)
		else:
			anagrams[sortedWord] = [word]
	return list(anagrams.values())




############################### 2 ###############################
# O(w*n*log(n) + n*w*log(w)) time | O(wn) space   ;w is number of words, n is maximum length of word
def groupAnagrams(words):
	if len(words) == 0:
		return []

	sortedWords = ["".join(sorted(w)) for w in words]
	indices = [i for i in range(len(words))]
	indices.sort(key = lambda x: sortedWords[x])

	result = []
	currentAnagramGroup = []
	currentAnagram = sortedWords[indices[0]]

	for index in indices:
		sortedWord = sortedWords[index]
		word = words[index]

		if currentAnagram == sortedWord:
			currentAnagramGroup.append(word)
			continue

		result.append(currentAnagramGroup)
		currentAnagramGroup = [word]
		currentAnagram = sortedWord

	result.append(currentAnagramGroup)
	return result

	# sortedWords = [("".join(sorted(x)),i) for i,x in enumerate(words)]
	# sortedWords.sort(key = lambda x: len(x[0]))
	# result = []
	# currentAnagramGroup = []
	# currentAnagram = sortedWords[0][0]
	# for tup in sortedWords:
	# 	if currentAnagram == tup[0]:
	# 		currentAnagramGroup.append(words[tup[1]])
	# 		continue

	# 	result.append(currentAnagramGroup)
	# 	currentAnagramGroup = [words[tup[1]]]
	# 	currentAnagram = tup[0]

	# result.append(currentAnagramGroup)
	# return result




print(groupAnagrams(["yo", "act", "flop", "tac", "cat", "oy", "olfp"]))
