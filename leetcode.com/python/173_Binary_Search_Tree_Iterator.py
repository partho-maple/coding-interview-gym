# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Approach 1: https://tinyurl.com/smu9ku3
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodesSorted = []
        self.nextIndex = 0
        self.__inorder(root)

    def __inorder(self, root):
        if not root:
            return
        self.__inorder(root.left)
        self.nodesSorted.append(root.val)
        self.__inorder(root.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        value = self.nodesSorted[self.nextIndex]
        self.nextIndex += 1
        return value

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.nextIndex < len(self.nodesSorted)


# Approach 2: https://tinyurl.com/smu9ku3
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.__leftMostInorder(root)

    def __leftMostInorder(self, root):
        curentStack = self.stack
        while root:
            curentStack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        curentStack = self.stack
        topMostNode = curentStack.pop()
        if topMostNode.right:
            self.__leftMostInorder(topMostNode.right)
        return topMostNode.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        curentStack = self.stack
        return len(curentStack) > 0