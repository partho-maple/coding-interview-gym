# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Approach 5. Source: https://tinyurl.com/rybqon6
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        numerOfLists = len(lists)
        interval = 1
        while interval < numerOfLists:
            for idx in range(0, numerOfLists - interval, interval * 2):
                lists[idx] = self.mergeTwoLists(lists[idx], lists[idx + interval])
            interval *= 2
        return lists[0] if numerOfLists > 0 else None


    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 if l1 else l2
        p1, p2, p1Prev = l1, l2, None
        while p1 and p2:
            if p1.val < p2.val:
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
        return l1 if l1.val < l2.val else l2
