def hasSingleCycle(array):
	numElementsVisited = 0
	startingIdx = 0
	currentIdx = startingIdx
	while numElementsVisited < len(array):
		if numElementsVisited > 0 and currentIdx == startingIdx:
			return False
		numElementsVisited += 1
		currentIdx = getNextIdx(currentIdx, array)
	return currentIdx == startingIdx

def getNextIdx(currentIdx, array):
	jump = array[currentIdx]
	nextIdx = (currentIdx + jump) % len(array)
	return nextIdx if nextIdx >= 0 else nextIdx + len(array) 

print(hasSingleCycle([2, 3, 1, -4, -4, 2]))