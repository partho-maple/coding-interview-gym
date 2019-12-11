# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        setG = set(G)
        result, count = 0, 0
        while head:
            if head.val in setG:
                count += 1
            else:
                if count:
                    result += 1
                count = 0
            head = head.next
        return result + 1 if count else result

