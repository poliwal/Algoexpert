######################## 1 #########################
# O(2^n) time | O(n) space
def nthFibonacci(n):
	if n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return nthFibonacci(n-1) + nthFibonacci(n-2)




######################## 2 #########################
# O(n) time | O(n) space
def nthFibonacci(n, memoize = {1: 0, 2: 1}):
	if n in memoize:
		return memoize[n]
	else:
		memoize[n] = nthFibonacci(n-1, memoize) + nthFibonacci(n-2, memoize)
		return memoize[n]




######################## 3 #########################
# O(2^n) time | O(n) space
def nthFibonacci(n):
	elem = [0, 1]
	counter = 2
	while counter < n:
		nextFib = elem[0] + elem[1]
		elem[0] = elem[1]
		elem[1] = nextFib
		counter += 1
	return elem[1] if n > 1 else elem[0]




print(nthFibonacci(1))