class Node:
	def __init__(self, name):
		self.children = []
		self.name = name

	def addChild(self, name):
		self.children.append(Node(name))
		return self
		
	# O(v + e) time | O(v) space
	def breadthFirstSearch(self, array):
		queue = [self]
		while len(queue) > 0:
			current = queue.pop(0)
			array.append(current.name)
			for child in current.children:
				queue.append(child)

		return array

result1 = []
test1 = Node("A")
test1.addChild("B").addChild("C")
test1.children[0].addChild("D")
test1.children[0].addChild("E")
print(test1.breadthFirstSearch(result1))

result2 = []
test2 = Node("A")
test2.addChild("B").addChild("C").addChild("D").addChild("E")
test2.children[1].addChild("F")
test2.children[1].children[0].addChild("Z")
print(test2.breadthFirstSearch(result2))