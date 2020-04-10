# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sums = []
    branchSumsHelper(root, root.value, sums)
    return sums


def branchSumsHelper(root, runningSum, sums):
    if not root.left and not root.right:
        sums.append(runningSum)
        return

    if root.left:
        runningSum += root.left.value
        branchSumsHelper(root.left, runningSum, sums)
        runningSum -= root.left.value

    if root.right:
        runningSum += root.right.value
        branchSumsHelper(root.right, runningSum, sums)
        runningSum -= root.right.value


