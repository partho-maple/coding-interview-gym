import collections


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    #   Solution 1: Recursive DFS
    # def minDepth(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if not root:
    #         return 0
    #     leftDepth = self.minDepth(root.left)
    #     rightDepth = self.minDepth(root.right)
    #     if not root.left or not root.right:
    #         return max(leftDepth, rightDepth) + 1  #  I'm trying to understand the use of max() in the DFS version. I think it's because if one of the node's children is None then in the next recursive call it would return zero but you don't want to count that because you know it is not actually a leaf so the max gets rid of the incorrect zero.
    #     else:
    #         return min(leftDepth, rightDepth) + 1

    #   Solution 2: Iterative DFS
    # def minDepth(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if not root:
    #         return 0
    #     result, stack = float("inf"), [(root, 1)]
    #     while stack:
    #         node, level = stack.pop()
    #         if node and not node.left and not node.right:
    #             result = min(result, level)
    #         if node:
    #             stack.append((node.left, level + 1))
    #             stack.append((node.right, level + 1))
    #     return result

    #   Solution 3: Iterative BFS
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result = 9999
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node and not node.left and not node.right:
                result = min(result, level)
            if node:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return result

