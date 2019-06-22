# https://leetcode.com/problems/closest-binary-search-tree-value


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
        return self


class Solution(object):

    def closestValue(self, root, target):
        return self.closestValueHelper(root, target, float("inf"))

    def closestValueHelper(self, root, target, closest):
        currentNode = root
        while currentNode is not None:
            t1 = abs(target - closest)
            t2 = abs(currentNode.val - target)
            if t1 > t2:
                closest = currentNode.val
            if target < currentNode.val:
                currentNode = currentNode.left
            elif target > currentNode.val:
                currentNode = currentNode.right
            else:
                break
        return closest


test_tree = TreeNode(4).insert(2).insert(5).insert(1).insert(3)
solution = Solution()

closest_val = solution.closestValue(test_tree, 3.714286)
print(str(closest_val) + " is the Closest Value")
