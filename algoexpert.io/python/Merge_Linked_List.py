# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    p1, p2 = headOne, headTwo
    p1Prev = None
    while p1 and p2:
        if p1.value < p2.value:
            p1Prev = p1
            p1 = p1.next
        else:
            if p1Prev:
                p1Prev.next = p2
            p1Prev = p2
            p2 = p2.next
            p1Prev.next = p1
    if not p1:
        p1Prev.next = p2
    return headOne if headOne.value < headTwo.value else headTwo



