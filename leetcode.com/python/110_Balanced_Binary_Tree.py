# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def check(node):
    if node == None:
        return (0, True)
    l_depth, l_balanced = check(node.left)
    r_depth, r_balanced = check(node.right)
    return max(l_depth, r_depth) + 1, l_balanced and r_balanced and abs(l_depth - r_depth) <= 1


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return check(root)[1]

