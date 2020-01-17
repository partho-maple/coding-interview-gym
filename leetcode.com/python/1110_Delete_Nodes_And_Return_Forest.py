# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        resultForest = []
        toDeleteSet = set(to_delete)
        self.removeNodesDFS(root, toDeleteSet, resultForest)
        if root.val not in toDeleteSet:
            resultForest.append(root)
        return resultForest


    def removeNodesDFS(self, root, toDeleteSet, resultForest):
        if not root:
            return None
        root.left = self.removeNodesDFS(root.left, toDeleteSet, resultForest)
        root.right = self.removeNodesDFS(root.right, toDeleteSet, resultForest)
        if root.val in toDeleteSet:
            if root.left:
                resultForest.append(root.left)
            if root.right:
                resultForest.append(root.right)
            return None
        return root

