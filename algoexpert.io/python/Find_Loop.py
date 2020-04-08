
# O(n) time | O(1) space
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def findLoop(head):
	if not head and not head.next:
		return None
    slowPtr, fastPtr = head.next, head.next.next
	while slowPtr != fastPtr:
		slowPtr = slowPtr.next
		fastPtr = fastPtr.next.next
	fastPtr = head
	while fastPtr != slowPtr:
		slowPtr = slowPtr.next
		fastPtr = fastPtr.next
	return fastPtr