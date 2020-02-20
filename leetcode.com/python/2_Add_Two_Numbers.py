# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        arr1, arr2 = [], []
        while l1:
            arr1.append(str(l1.val))
            l1 = l1.next
        while l2:
            arr2.append(str(l2.val))
            l2 = l2.next
        num1, num2 = int("".join(arr1[::-1])), int("".join(arr2[::-1]))
        finalNum = num1 + num2
        finalNumArr = list(str(finalNum))[::-1]
        dummyHead = ListNode(-1)
        head = ListNode(finalNumArr[0])
        dummyHead.next = head
        for i in range(1, len(finalNumArr)):
            node = ListNode(finalNumArr[i])
            head.next = node
            head = head.next
        return dummyHead.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next