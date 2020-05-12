#Time: O(n) | Space: O(n)
def twoNumberSum(Array, targetSum):
    hashTable = {}
    for i in Array:
        if (targetSum-i) in hashTable:
            return [targetSum-i,i]
        else:
            hashTable[i] = True
    return []


#Time: O(nlogn) | Space: O(1)
def twoNumberSum(Array,targetSum):
	Array.sort()
	l = 0
	r = len(Array)-1
	while l<r:
		if Array[l]+Array[r]<targetSum:
			l+=1
		elif Array[l]+Array[r]>targetSum:
			r+=1
		else:
			return [Array[l],Array[r]]
	return []

#Time: O(n^2) | Space: O(1)
def twoNumberSum(Array, targetSum):
    for i in range(len(Array)-1):
    	for j in range(i+1,len(Array)):
    		if Array[i]+Array[j] == targetSum:
	            return [Array[i],Array[j]]
    return []



print(twoNumberSum([1,2,3,4,5,6,7],9))
