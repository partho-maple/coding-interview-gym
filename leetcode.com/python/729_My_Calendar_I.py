class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, start, end):
        if self.start >= end:
            if self.left:
                return self.left.insert(start, end)
            else:
                self.left = TreeNode(start, end)
                return True
        elif self.end <= start:
            if self.right:
                return self.right.insert(start, end)
            else:
                self.right = TreeNode(start, end)
                return True
        else:
            return False

class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = TreeNode(start, end)
            return True
        return self.root.insert(start, end)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)