# O(n) time | O(n) space
def minHeightBst(array):
	return constructMinHeightBst(array, 0, len(array) - 1)

def constructMinHeightBst(array, startIdx, endIdx, bst = None):
	if endIdx < startIdx:
		return 
	midIdx = (startIdx + endIdx) // 2
	newBstNode = BST(array[midIdx])
	if bst is None:
		bst = newBstNode
	else:
		if array[midIdx] < bst.value:
			bst.left = newBstNode
			bst = bst.left
		else:
			bst.right = newBstNode
			bst = bst.right
	constructMinHeightBst(array, startIdx, midIdx - 1, bst)
	constructMinHeightBst(array, midIdx + 1, endIdx, bst)
	return bst

### Alternate way ###
# def constructMinHeightBst(array, startIdx, endIdx):
# 	if endIdx < startIdx:
# 		return None
# 	midIdx = (startIdx + endIdx) // 2
# 	bst = BST(array[midIdx])
# 	bst.left = constructMinHeightBst(array, startIdx, midIdx - 1)
# 	bst.right = constructMinHeightBst(array, midIdx + 1, endIdx)
# 	return bst

class BST:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None




print(minHeightBst([1,2,5,7,10,13,14,15,22]).value)