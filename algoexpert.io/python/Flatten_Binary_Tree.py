# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def flattenBinaryTree(root):
    iorderNodes = getNodesInOrder(root, [])
    for i in range(0, len(iorderNodes) - 1):
        leftNode = iorderNodes[i]
        rightNode = iorderNodes[i + 1]
        leftNode.right = rightNode
        rightNode.left = leftNode
    return iorderNodes[0]


def getNodesInOrder(tree, array):
    if tree is not None:
        getNodesInOrder(tree.left, array)
        array.append(tree)
        getNodesInOrder(tree.right, array)
    return array

