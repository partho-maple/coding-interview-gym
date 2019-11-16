# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        sortedArray = []
        self.getArrayFromLinkedList(head, sortedArray)
        return self.sortedListToBSTHelper(sortedArray, 0, len(sortedArray) - 1)

    def getArrayFromLinkedList(self, listHead, array):
        if not listHead:
            return
        else:
            array.append(listHead.val)
            self.getArrayFromLinkedList(listHead.next, array)

    def sortedListToBSTHelper(self, sortedArray, left, right):
        if left > right:
            return None
        rootIdx = (left + right) // 2
        rootNode = TreeNode(sortedArray[rootIdx])
        rootNode.left = self.sortedListToBSTHelper(sortedArray, left, rootIdx - 1)
        rootNode.right = self.sortedListToBSTHelper(sortedArray, rootIdx + 1, right)
        return rootNode

