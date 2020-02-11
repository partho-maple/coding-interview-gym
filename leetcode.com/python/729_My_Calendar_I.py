class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar(object):

    def __init__(self):
        self.root = None

    def bookHelper(self, start, end, node):
        if start >= node.end:
            if node.right:
                return self.bookHelper(start, end, node.right)
            else:
                node.right = TreeNode(start, end)
                return True
        elif end <= node.start:
            if node.left:
                return self.bookHelper(start, end, node.left)
            else:
                node.left = TreeNode(start, end)
                return True
        else:
            return False

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = TreeNode(start, end)
            return True
        return self.bookHelper(start, end, self.root)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)