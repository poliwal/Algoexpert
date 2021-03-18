############################## Method-1 #################################
# O(n) time | O(1) space
def isMonotonicArray1(array):
	isNonIncreasing = True
	isNonDecreasing = True
	for i in range(1,len(array)):
		if array[i] > array[i-1]:
			isNonIncreasing = False
		if array[i] < array[i-1]:
			isNonDecreasing = False

	return isNonDecreasing or isNonIncreasing




############################## Method-2 #################################
# O(n) time | O(1) space
def isMonotonicArray2(array):
	if len(array)<=2:
		return True

	direction = array[1] - array[0]
	for i in range(2,len(array)):
		if direction==0:
			direction = array[i] - array[i-1]
			continue
		if breaksDirection(direction, array[i-1], array[i]):
			return False

	return True 

def breaksDirection(direction, prev, curr):
	difference = curr - prev
	print(difference<0)
	if direction > 0:
		return difference<0
	return difference>0





print(isMonotonicArray1([1,2,3,3,4,4,5,6]))
print(isMonotonicArray2([1,2,3,3,4,4,5,6]))
