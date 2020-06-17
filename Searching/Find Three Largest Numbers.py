# O(n) time | O(1) space 
def findThreeLargestNumbers(array):
	threeLargest = [None, None, None]
	for num in array:
		updateLargest(threeLargest, num)
	return threeLargest

def updateLargest(threeLargest, num):
	if threeLargest[2] == None or threeLargest[2] < num:
		shiftAndUpdate(threeLargest, num, 2)
	elif threeLargest[1] == None or threeLargest[1] < num:
		shiftAndUpdate(threeLargest, num, 1)
	elif threeLargest[0] == None or threeLargest[0] < num:
		shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(threeLargest, num, idx):
	for i in range(idx + 1):
		if i == idx:
			threeLargest[i] = num
		else:
			threeLargest[i] = threeLargest[i + 1]

print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))