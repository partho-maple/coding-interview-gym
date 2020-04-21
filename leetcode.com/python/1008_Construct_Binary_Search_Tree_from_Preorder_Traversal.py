# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        inorder = sorted(preorder)
        inorderMap = {val: i for i, val in enumerate(inorder)}
        return self.bstFromPreorderHelper(preorder, inorderMap, 0, len(inorder) - 1)

    def bstFromPreorderHelper(self, preorder, inorderMap, inorderLeftIdx, inorderRightIdx):
	    if not preorder:
	        return None
	    rootVal = preorder.pop(0)
	    rootIdxInInorder = inorderMap[rootVal]
	    root = TreeNode(rootVal)
	    if inorderLeftIdx < rootIdxInInorder:
	        root.left = self.bstFromPreorderHelper(preorder, inorderMap, inorderLeftIdx, rootIdxInInorder - 1)
	    if inorderRightIdx > rootIdxInInorder:
	        root.right = self.bstFromPreorderHelper(preorder, inorderMap, rootIdxInInorder + 1, inorderRightIdx)
	    return root
