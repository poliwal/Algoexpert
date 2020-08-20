#Average: O(log(n)) time | O(1) space
#Worst: O(n) time | O(1) space
def findClosestValueInBST(tree, target):
	closest = float("inf")
	currentNode = tree
	while currentNode is not None:
		if abs(target - closest) > (target - currentNode.value):
			closest = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break
	return closest