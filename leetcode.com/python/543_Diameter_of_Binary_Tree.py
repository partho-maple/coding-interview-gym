# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.treeDiameter = 0
        self.diameterOfBinaryTreeHelper(root)
        return self.treeDiameter

    def diameterOfBinaryTreeHelper(self, currentNode):
        if not currentNode:
            return 0
        leftSubTreeMaxHeight = self.diameterOfBinaryTreeHelper(currentNode.left)
        rightSubTreeMaxHeight = self.diameterOfBinaryTreeHelper(currentNode.right)
        currentDiameter = leftSubTreeMaxHeight + rightSubTreeMaxHeight
        self.treeDiameter = max(self.treeDiameter, currentDiameter)
        currentNodeMaxHeight = max(leftSubTreeMaxHeight, rightSubTreeMaxHeight) + 1
        return currentNodeMaxHeight
