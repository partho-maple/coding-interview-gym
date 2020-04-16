# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countDepth(self, node):
        depth = 0
        while node.left:
            node = node.left
            depth += 1
        return depth

    def exists(self, index, depth, node):
        left, right = 0, 2 ** depth - 1
        for _ in range(depth):
            pivot = left + (right - left) // 2
            if index <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return False if not node else True

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = self.countDepth(root)
        if depth == 0:
            return 1
        left, right = 0, 2 ** depth - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, depth, root):
                left = pivot + 1
            else:
                right = pivot - 1
        return (2 ** depth - 1) + left


# My solution during Leetcode Mock Interview
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftCount = self.countNodes(root.left)
        rightCount = self.countNodes(root.right)
        totalCount = leftCount + 1 + rightCount
        return totalCount