# O(n) time | O(1) space
def removeKthFromEnd(head, k):
	first = head
	second = head
	counter = 1
	while counter <= k:
		second = second.next
		counter += 1
	if second is None:
		head.next = head.next.next
		return
	while second.next is not None:
		second = second.next
		first = first.next
	first.next = first.next.next

class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
   
class LinkedList: 
    def __init__(self):  
        self.head = None

    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data,end='\t') 
            temp = temp.next
        print("")

first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)

LL = LinkedList()
LL.head = first
LL.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

LL.printList()

removeKthFromEnd(LL.head, 3)

LL.printList()