
#   Solution 1: Binary Search Tree
class BinarySearchTreeNode(object):
    def __init__(self,  val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.leftTreeSize = 0


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val, root):
        if not root:
            self.root = BinarySearchTreeNode(val)
            return 0
        if val == root.val:
            root.count += 1
            return root.leftTreeSize
        if val < root.val:
            root.leftTreeSize += 1
            if not root.left:
                root.left = BinarySearchTreeNode(val)
                return 0
            return self.insert(val, root.left)
        if not root.right:
            root.right = BinarySearchTreeNode(val)
            return root.count + root.leftTreeSize
        return root.count + root.leftTreeSize + self.insert(val, root.right)


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tree = BinarySearchTree()
        counts = []
        for i in range(len(nums) - 1, -1, -1):
            counts.append(tree.insert(nums[i], tree.root))
        return counts[::-1]





sol = Solution()
input = [5,2,6,1]
output = sol.countSmaller(input)
print("Res: ", output)