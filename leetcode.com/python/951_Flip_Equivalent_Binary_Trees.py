# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        if not self.sameChildren(root1, root2):
            temp = root1.left
            root1.left = root1.right
            root1.right = temp
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)


    def sameChildren(self, root1, root2):
        sameLeft, sameRight = False, False
        if not root1.left and not root2.left:
            sameLeft = True
        elif not root1.left or not root2.left:
            sameLeft = False
        else:
            sameLeft = root1.left.val == root2.left.val

        if not root1.right and not root2.right:
            sameRight = True
        elif not root1.right or not root2.right:
            sameRight = False
        else:
            sameRight = root1.right.val == root2.right.val

        return sameLeft and sameRight


