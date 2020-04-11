# O(n) time | O(1) space
def reverseLinkedList(head):
    prevN, nextN = None, None
	while head is not None:
		nextN = head.next
		head.next = prevN
		prevN = head
		head = nextN
	return prevN