
# O(n) time | O(1) space
def reverseLinkedList(head):
    p1, p2 = None, head
    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    return p1