# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [], []
        currentNode = root
        while currentNode is not None or len(stack) > 0:
            while currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.left
            currentNode = stack.pop()
            result.append(currentNode.val)
            currentNode = currentNode.right
        return result


# Solution 2
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [], []
        currentNode = root
        while currentNode is not None or len(stack) > 0:
            if currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.left
            else:
                currentNode = stack.pop()
                result.append(currentNode.val)
                currentNode = currentNode.right
        return result





