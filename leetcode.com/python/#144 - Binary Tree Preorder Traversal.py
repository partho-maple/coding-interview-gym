# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# S0lution 1
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [root, ], []
        while len(stack) > 0:
            currentNode = stack.pop()
            if currentNode is not None:
                result.append(currentNode.val)
                if currentNode.right is not None:
                    stack.append(currentNode.right)
                if currentNode.left is not None:
                    stack.append(currentNode.left)
        return result


# S0lution 2
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [], []
        currentNode = root
        while currentNode or len(stack) > 0:
            if currentNode:
                result.append(currentNode.val)
                stack.append(currentNode.right)
                stack.append(currentNode.left)
            currentNode = stack.pop()
        return result
