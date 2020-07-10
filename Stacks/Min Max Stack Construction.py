class MixMaxStack:
	def __init__(self):
		self.minMaxStack = []
		self.stack = []

	# O(1) time | O(1) space
	def peek(self):
		return self.stack[-1]

	# O(1) time | O(1) space
	def pop(self):
		self.minMaxStack.pop()
		return self.stack.pop()
	
	# O(1) time | O(1) space	
	def push(self, num):
		newMinMax = {'min': num, 'max': num}
		if len(self.minMaxStack):
			newMinMax['min'] = min(self.minMaxStack[-1]['min'], num)
			newMinMax['max'] = max(self.minMaxStack[-1]['max'], num)
		self.minMaxStack.append(newMinMax)
		self.stack.append(num)
	
	# O(1) time | O(1) space
	def getMin(self):
		return self.minMaxStack[-1]['min']
	
	# O(1) time | O(1) space
	def getMax(self):
		return self.minMaxStack[-1]['max']
