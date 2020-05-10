# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My initial approacch
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        startingNodesOnS = []
        self.getStartingNodeOnS(s, t.val, startingNodesOnS)
        if len(startingNodesOnS) <= 0:
            return False

        for node in startingNodesOnS:
            if self.isSameTree(node, t):
                return True
        return False

    def getStartingNodeOnS(self, s, tVal, startingNodesOnS):
        if not s:
            return
        if s.val == tVal:
            startingNodesOnS.append(s)
        leftNode = self.getStartingNodeOnS(s.left, tVal, startingNodesOnS)
        rightNode = self.getStartingNodeOnS(s.right, tVal, startingNodesOnS)
        if leftNode:
            startingNodesOnS.append(leftNode)
            return
        elif rightNode:
            startingNodesOnS.append(rightNode)
            return
        else:
            return

    def isSameTree(self, startingNodeOnS, t):
        if not startingNodeOnS and not t:
            return True
        if startingNodeOnS and t and startingNodeOnS.val == t.val:
            left = self.isSameTree(startingNodeOnS.left, t.left)
            right = self.isSameTree(startingNodeOnS.right, t.right)
            return left and right
        else:
            return False


