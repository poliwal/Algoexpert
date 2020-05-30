# O(d) time ;d is depth of lowest descendant | O(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = getDescendantDepth(topAncestor, descendantOne)
	depthTwo = getDescendantDepth(topAncestor, descendantTwo)
	if depthOne > depthTwo:
		return backTrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
	else:
		return backTrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)

def getDescendantDepth(topAncestor, descendant):
	depth = 0
	while descendant != topAncestor:
		depth += 1
		descendant = descendant.ancestor
	return depth

def backTrackAncestralTree(lowerDescendant, higherDescendant, diff):
	while diff > 0:
		lowerDescendant = lowerDescendant.ancestor
		diff -= 1
	while lowerDescendant != higherDescendant:
		lowerDescendant = lowerDescendant.ancestor
		higherDescendant = higherDescendant.ancestor
	return lowerDescendant.name

class Node:
	def __init__(self, name):
		self.ancestor = ""
		self.name = name

	def addAncestor(self, ancestor):
		self.ancestor = ancestor

a = Node('A')
b = Node('B')
g = Node('G')
h = Node('H')
i = Node('I')
o = Node('O')
p = Node('P')
q = Node('Q')
t = Node('T')
u = Node('U')

i.addAncestor(b)
t.addAncestor(p)
u.addAncestor(p)
p.addAncestor(h)
o.addAncestor(h)
q.addAncestor(h)
h.addAncestor(b)
g.addAncestor(b)
i.addAncestor(b)
b.addAncestor(a)

print(getYoungestCommonAncestor(a, i, t))