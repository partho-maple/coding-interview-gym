# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# The first value of 'pre' and last value of 'post' is 'root'.
# Find the second value of 'pre' in 'post' as it is the left child of 'root'.
# From here, we divide pre and post into left branch and right branch.
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if pre:
            root = TreeNode(pre.pop(0))
            post.pop()
            if pre:
                if pre[0] == post[-1]:
                    root.left = self.constructFromPrePost(pre, post)
                else:
                    l, r = post.index(pre[0]), pre.index(post[-1])
                    root.left = self.constructFromPrePost(pre[:r], post[:l + 1])
                    root.right = self.constructFromPrePost(pre[r:], post[l + 1:])
            return root
