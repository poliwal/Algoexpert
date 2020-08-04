# O(n) time | O(1) space
def reverseLinkedList(head):
	prev, curr = None,head
	while curr is not None:
		nextNode = curr.next
		curr.next = prev
		prev = curr
		curr = nextNode
	return prev
   