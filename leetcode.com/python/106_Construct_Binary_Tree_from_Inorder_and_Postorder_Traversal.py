# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# # Approach 1, using  recursion, Accepted.  But check: https://tinyurl.com/vlntqrp
# class Solution(object):
#     def buildTree(self, inorder, postorder):
#         """
#         :type inorder: List[int]
#         :type postorder: List[int]
#         :rtype: TreeNode
#         """
#         if not inorder or not postorder:
#             return None
#         root = TreeNode(postorder.pop())
#         rootIdxFromInorder = inorder.index(root.val)
#         root.right = self.buildTree(inorder[rootIdxFromInorder + 1:], postorder)
#         root.left = self.buildTree(inorder[:rootIdxFromInorder], postorder)
#         return root




class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inorderMap = {}
        for idx, value in enumerate(inorder):
            inorderMap[value] = idx
        return self.buildTreeHelper(inorder, postorder, inorderMap)


    def buildTreeHelper(self, inorder, postorder, inorderMap):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        # rootIdxFromInorder = inorderMap[root.val]
        rootIdxFromInorder = inorder.index(root.val)
        root.right = self.buildTreeHelper(inorder[rootIdxFromInorder + 1:], postorder, inorderMap)
        root.left = self.buildTreeHelper(inorder[:rootIdxFromInorder], postorder, inorderMap)
        return root




sol = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
out = sol.buildTree(inorder, postorder)
print("Res: ", out)