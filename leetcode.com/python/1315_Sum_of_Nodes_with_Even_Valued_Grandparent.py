# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Top-Down
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.nodeSumGlobal = 0
        self.sumEvenGrandparentHelper(root, None, None)
        return self.nodeSumGlobal

    def sumEvenGrandparentHelper(self, root, parent, grandParent):
        if not root:
            return 0
        if grandParent and (grandParent.val % 2 == 0):
            self.nodeSumGlobal += root.val

        self.sumEvenGrandparentHelper(root.left, root, parent)
        self.sumEvenGrandparentHelper(root.right, root, parent)


# Bottom-Up
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodeSum = self.sumEvenGrandparentHelper(root, None, None)
        return nodeSum

    def sumEvenGrandparentHelper(self, root, parent, grandParent):
        if not root:
            return 0

        left = self.sumEvenGrandparentHelper(root.left, root, parent)
        right = self.sumEvenGrandparentHelper(root.right, root, parent)

        currentSum = left + right
        if grandParent and (grandParent.val % 2 == 0):
            currentSum += root.val
        return currentSum
