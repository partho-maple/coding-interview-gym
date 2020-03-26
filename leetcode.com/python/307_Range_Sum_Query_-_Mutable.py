# Source:   https://tinyurl.com/srucx8l
"""
    The idea here is to build a segment tree. Each node stores the left and right
    endpoint of an interval and the sum of that interval. All of the leaves will store
    elements of the array and each internal node will store sum of leaves under it.
    Creating the tree takes O(n) time. Query and updates are both O(log n).
"""

# Segment Tree Node
class Node(object):
    def __init__(self, rangeStart, rangeEnd):
        self.rangeStart = rangeStart
        self.rangeEnd = rangeEnd
        self.rangeSum = 0
        self.leftNode = None
        self.rightNode = None


class NumArray(object):

    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.root = self.createTree(nums, 0, len(nums) - 1)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.updateHelper(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumRangeHelper(self.root, i, j)

    # helper function to create the tree from input array
    def createTree(self, nums, rangeStart, rangeEnd):
        # base case
        if rangeStart > rangeEnd:
            return None

        # leaf node
        if rangeStart == rangeEnd:
            node = Node(rangeStart, rangeEnd)
            node.rangeSum = nums[rangeStart]
            return node

        mid = (rangeStart + rangeEnd) // 2
        currentRoot = Node(rangeStart, rangeEnd)

        # recursively build the Segment tree
        currentRoot.leftNode = self.createTree(nums, rangeStart, mid)
        currentRoot.rightNode = self.createTree(nums, mid + 1, rangeEnd)

        # Total stores the sum of all leaves under root
        # i.e. those elements lying between (rangeStart, rangeEnd)
        currentRoot.rangeSum = currentRoot.leftNode.rangeSum + currentRoot.rightNode.rangeSum

        return currentRoot

    # Helper function to update a value
    def updateHelper(self, root, index, value):
        # Base case. The actual value will be updated in a leaf.
        # The total is then propogated upwards
        if root.rangeStart == root.rangeEnd:
            root.rangeSum = value
            return root.rangeSum

        mid = (root.rangeStart + root.rangeEnd) // 2

        # If the index is less than the mid, that leaf must be in the left subtree
        if index <= mid:
            self.updateHelper(root.leftNode, index, value)
        else:   #Otherwise, the right subtree
            self.updateHelper(root.rightNode, index, value)

        # Propogate the changes after recursive call returns
        root.rangeSum = root.leftNode.rangeSum + root.rightNode.rangeSum

        return root.rangeSum

    # Helper function to calculate range sum
    def sumRangeHelper(self, root, rangeStart, rangeEnd):
        # If the range exactly matches the root, we already have the sum
        if root.rangeStart == rangeStart and root.rangeEnd == rangeEnd:
            return root.rangeSum

        mid = (root.rangeStart + root.rangeEnd) // 2

        if rangeEnd <= mid:        # If end of the range is less than the mid, the entire interval lies in the left subtree
            return self.sumRangeHelper(root.leftNode, rangeStart, rangeEnd)
        elif rangeStart >= mid + 1: # If start of the interval is greater than mid, the entire inteval lies in the right subtree
            return self.sumRangeHelper(root.rightNode, rangeStart, rangeEnd)
        else:   # Otherwise, the interval is split. So we calculate the sum recursively, by splitting the interval
            return self.sumRangeHelper(root.leftNode, rangeStart, mid) + self.sumRangeHelper(root.rightNode, mid + 1, rangeEnd)








# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)