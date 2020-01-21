# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findNode(self, nodeVal, root):
        if not root:
            return None
        if root.val == nodeVal:
            return root
        left = self.findNode(nodeVal, root.left)
        if left:
            return left
        else:
            return self.findNode(nodeVal, root.right)

    def countNode(self, root):
        if not root:
            return 0
        leftCount = self.countNode(root.left)
        rightCount = self.countNode(root.right)
        return leftCount + rightCount + 1

    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        xNode = self.findNode(x, root)
        xNodeLeftCount = self.countNode(xNode.left)
        xNodeRightCount = self.countNode(xNode.right)
        xNodeParentCount = n - xNodeLeftCount - xNodeRightCount - 1
        return any([xNodeParentCount > xNodeLeftCount + xNodeRightCount,
                    xNodeLeftCount > xNodeRightCount + xNodeParentCount,
                    xNodeRightCount > xNodeLeftCount + xNodeParentCount])
