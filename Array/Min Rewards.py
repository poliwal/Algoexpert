####################### Method 1 ###########################
# O(n^2) time | O(n) space
def minRewards(scores):
	rewards = [1 for _ in scores]
	for i in range(1, len(scores)):
		j = i - 1
		if scores[i] > scores[j]:
			rewards[i] = rewards[j] + 1
		else:
			while j>=0 and scores[j] > scores[j+1]:
				rewards[j] = max(rewards[j], rewards[j+1] + 1)
				j -= 1

	return sum(rewards)




####################### Method 2 ###########################
# O(n) time | O(n) space
def minRewards(scores):
	rewards = [1 for _ in scores]
	localMinIndices = getLocalMinIndices(scores)
	for localMinIndex in localMinIndices:
		expandFromLocalMinIndex(localMinIndex, scores, rewards)

	return sum(rewards)

def getLocalMinIndices(scores):
	if len(scores) == 1:
		return [0]
	localMinIndices = []
	for i in range(len(scores)):
		if i == 0 and scores[i] < scores[i + 1]:
			localMinIndices.append(i)
		if i == len(scores) - 1 and scores[i] < scores[i - 1]:
			localMinIndices.append(i)
		if i == 0 or i == len(scores) - 1:
			continue
		if scores[i] < scores[i + 1] and scores[i] < scores[i - 1]:
			localMinIndices.append(i)
	return localMinIndices

def expandFromLocalMinIndex(localMinIndex, scores, rewards):
	left = localMinIndex - 1
	right = localMinIndex + 1
	while left >= 0 and scores[left] > scores[left + 1]:
		rewards[left] = max(rewards[left], rewards[left + 1] + 1)
		left -= 1
	while right < len(scores) and scores[right] > scores[right - 1]:
		rewards[right] = rewards[right - 1] + 1
		right += 1 




####################### Method 2 ###########################
# O(n) time | O(n) space
def minRewards(scores):
	rewards = [1 for _ in scores]
	for i in range(1, len(scores)):
		if scores[i] > scores[i - 1]:
			rewards[i] = rewards[i - 1] + 1
	for i in range(len(scores)-2, -1, -1):
		if scores[i] > scores[i + 1]:
			rewards[i] = max(rewards[i], rewards[i+1] + 1)

	return sum(rewards)




print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))