# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Some notes:
# The reason why it is post-order is,
# you will never know how many coins to move to your parents until you figure out the number of your left & right branches' needed coins.

# # Uses global variable
# class Solution(object):
#     def distributeCoins(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         self.transactionCount = 0
#         self.distributeCoinsHelper(root)
#         return self.transactionCount
#
#     def distributeCoinsHelper(self, root):
#         if not root:
#             return 0
#         leftTreeCoin = self.distributeCoinsHelper(root.left)  # Coin balance from left tree
#         rightTreeCoin = self.distributeCoinsHelper(root.right) # Coin balance from right tree
#         self.transactionCount += abs(leftTreeCoin) + abs(rightTreeCoin)
#         return root.val + leftTreeCoin + rightTreeCoin - 1  # returning own coin balance to it's parent that is being given


# Give the parent node so we can move the coins to the parent directly. But it mutates the input tree, which is not great. But this one is  very intuitive
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.distributeCoinsHelper(root, parentNode=None)

    def distributeCoinsHelper(self, root, parentNode):
        if not root:
            return 0
        transactionCount = self.distributeCoinsHelper(root.left, root) + self.distributeCoinsHelper(root.right, root)
        if parentNode:
            parentNode.val += root.val - 1
        return transactionCount + abs(root.val - 1)  # returning own coin balance to it's parent that is being given



# From: https://tinyurl.com/s62fws7
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.distributeCoinsHelper(root)[1]

    def distributeCoinsHelper(self, root):
        if not root:
            return (0, 0)
        leftBalance, leftMoveCount = self.distributeCoinsHelper(root.left)
        rightBalance, rightMoveCount = self.distributeCoinsHelper(root.right)
        nodeBalance = root.val + leftBalance + rightBalance - 1
        nodeMoveCountThusFar = leftMoveCount + rightMoveCount + abs(nodeBalance)
        return (nodeBalance, nodeMoveCountThusFar)



sol = Solution()
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(0)
root.left.right = TreeNode(3)
output = sol.distributeCoins(root)
print("Res: ", output)