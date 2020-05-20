################################## Approach 1 #####################################
# O(b^2 * r) time | O(b) space
def apartmentHunting(blocks, requirements):
	maxDistancesAtBlocks = [float("-inf") for _ in blocks]
	for i in range(len(blocks)):
		for requirement in requirements:
			closestRequirementDistance = float('inf')
			for j in range(len(blocks)):
				if blocks[j][requirement]:
					closestRequirementDistance = min(closestRequirementDistance, getDistanceBetween(i, j))
			maxDistancesAtBlocks[i] = max(closestRequirementDistance, maxDistancesAtBlocks[i])
	return maxDistancesAtBlocks.index(min(maxDistancesAtBlocks))

def getDistanceBetween(i, j):
	return abs(i - j)




################################## Approach 2 #####################################
# O(b * r) time | O(br) space
def apartmentHunting(blocks, requirements):
	minDistancesFromBlocks = list(map(lambda requirement: getMinDistances(blocks, requirement), requirements))
	maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)
	return maxDistancesAtBlocks.index(min(maxDistancesAtBlocks))

def getDistanceBetween(i, j):
	return abs(i - j)

def getMinDistances(blocks, requirement):
	minDistances = [0 for _ in blocks]
	closestRequirementIndex = float("inf")
	for i in range(len(blocks)):
		if blocks[i][requirement]:
			closestRequirementIndex = i
		minDistances[i] = getDistanceBetween(i, closestRequirementIndex)
	for i in range(len(blocks)-1, -1, -1):
		if blocks[i][requirement]:
			closestRequirementIndex = i
		minDistances[i] = min(minDistances[i], getDistanceBetween(i, closestRequirementIndex))
	return minDistances

def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
	maxDistancesAtBlocks = [0 for _ in blocks]
	for i in range(len(blocks)):
		minDistancesAtBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))
		maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
	return maxDistancesAtBlocks




print(apartmentHunting([ { "gym": False, "school": True, "store": False, }, { "gym": True, "school": False, "store": False, }, { "gym": True, "school": True, "store": False, }, { "gym": False, "school": True, "store": False, }, { "gym": False, "school": True, "store": True, }, ], ["gym","school","store"]))