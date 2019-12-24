# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generate_trees(1, n) if n else []

    def generate_trees(self, start, end):
        if start > end:
            return [None, ]

        all_trees = []
        for i in range(start, end + 1):  # pickup a root

            # all possible left subbtrees if i is choosen to be a root
            left_trees = self.generate_trees(start, i - 1)

            # all possible right subbtrees if i is choosen to be a root
            right_trees = self.generate_trees(i + 1, end)

            # connect left and right subtree to root i
            for left_tree in left_trees:
                for right_tree in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = left_tree
                    current_tree.right = right_tree
                    all_trees.append(current_tree)

        return all_trees
