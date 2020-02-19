"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


# Idea: preorder recursive traversal; add number of children after root val, in order to know when to terminate.
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        nodeList = []
        self.serializeHelper(root, nodeList)
        return ','.join(map(str, nodeList))


    def serializeHelper(self, root, nodeList):
        if root is None:
            return
        nodeList.append(root.val)
        nodeList.append(len(root.children))
        for child in root.children:
            self.serializeHelper(child, nodeList)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if len(data) <= 0:
            return None
        nodeList = data.split(",")
        currentNodeIndexs = [0]
        deserializedData = self.deserializeHelper(nodeList, currentNodeIndexs)
        return deserializedData


    def deserializeHelper(self, nodeList, currentNodeIndexs):
        if currentNodeIndexs[0] == len(nodeList):
            return None
        root = Node(int(nodeList[currentNodeIndexs[0]]), [])
        currentNodeIndexs[0] += 1
        childrenSize = int(nodeList[currentNodeIndexs[0]])
        currentNodeIndexs[0] += 1
        for index in range(childrenSize):
            root.children.append(self.deserializeHelper(nodeList, currentNodeIndexs))
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))