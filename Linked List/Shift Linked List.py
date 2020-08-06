# O(n) time | O(1) space
def shiftLinkedList(head, k):
	listLength = 1
	listTail = head
	while listTail is not None:
		prev = listTail
		listTail = listTail.next
		if listTail is not None:
			listLength += 1
	
	offset = abs(k) % listLength
	if offset == 0:
		return head

	newTailPosition = listLength - offset if k > 0 else offset
	newTail = head
	for i in range(1,newTailPosition):
		newTail = newTail.next

	newHead = newTail.next
	newTail.next = None
	prev.next = head
	return newHead
