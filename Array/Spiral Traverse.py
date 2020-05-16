################################ Iterative ##################################
# O(N) time | O(N) space ;N is total number of elements in matrix 
def spiralTraverse(array):
	result = []
	startRow, endRow = 0, len(array)-1
	startColumn, endColumn = 0, len(array[0])-1

	while startRow <= endRow and startColumn <= endColumn:
		for col in range(startColumn, endColumn+1):
			result.append(array[startRow][col])

		for row in range(startRow+1, endRow+1):
			result.append(array[row][endColumn])

		for col in range(endColumn-1, startColumn-1, -1):
			result.append(array[endRow][col])

		for row in range(endRow-1, startRow, -1):
			result.append(array[row][startColumn])

		startRow += 1
		endRow -= 1
		startColumn += 1
		endColumn -= 1

	return result


################################ Recursive ##################################
# O(N) time | O(N) space ;N is total number of elements in matrix
def spiralTraverse(array):
	result = []
	spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
	return result

def spiralFill(array, startRow, endRow, startColumn, endColumn, result):
	if startRow > endRow or startColumn > endColumn:
		return

	for col in range(startColumn, endColumn+1):
		result.append(array[startRow][col])

	for row in range(startRow+1, endRow+1):
		result.append(array[row][endColumn])

	for col in range(endColumn-1, startColumn-1, -1):
		result.append(array[endRow][col])

	for row in range(endRow-1, startRow, -1):
		result.append(array[row][startColumn])
	
	spiralFill(array, startRow + 1, endRow - 1, startColumn + 1, endColumn - 1, result)



print(spiralTraverse([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))