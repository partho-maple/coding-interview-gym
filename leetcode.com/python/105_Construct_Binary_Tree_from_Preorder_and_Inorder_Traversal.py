# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        rootIdxIntoInorder = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:], inorder[:rootIdxIntoInorder])
        root.right = self.buildTree(preorder[rootIdxIntoInorder + 1:], inorder[rootIdxIntoInorder + 1:])
        return root


sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
out = sol.buildTree(preorder, inorder)
print("Res: ", out)

