##################################### 1 ####################################
# O(n^2*n!) time | O(n*n!) space
def getPermutations(array):
	permutations = []
	permutationsHelper(array, [], permutations)
	return permutations

def permutationsHelper(array, currentPermutation, permutations):
	if not len(array) and len(currentPermutation):
		permutations.append(currentPermutation)
	else:
		for i in range(len(array)):
			newArray = array[:i] + array[i + 1:]
			newPermutations = currentPermutation + [array[i]]
			print(newArray, newPermutations)
			permutationsHelper(newArray, newPermutations, permutations)




##################################### 2 ####################################
# O(n*n!) time | O(n*n!) space
def getPermutations(array):
	permutations = []
	permutationsHelper(0, array, permutations)
	return permutations

def permutationsHelper(i, array, permutations):
	if i == len(array) - 1:
		permutations.append(array[:])
	else:
		for j in range(i, len(array)):
			array[i], array[j] = array[j], array[i]
			permutationsHelper(i + 1, array, permutations)		
			array[i], array[j] = array[j], array[i]	




print(getPermutations([1, 2, 3]))