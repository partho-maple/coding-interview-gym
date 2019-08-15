"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


# Idea: preorder recursive traversal; add number of children after root val, in order to know when to terminate.
# Example: The example in description is serialized as: "1,3,3,2,5,0,6,0,2,0,4,0"
# Ref: https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/151421/Java-preorder-recursive-solution-using-queue/169724

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        nodeList = []
        self.serializeHelper(root, nodeList)
        # print('Serialized Input: ', ','.join(map(str, nodeList)))
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
        indexs = [0]
        deserializedData = self.deserializeHelper(nodeList, indexs)
        # print('Deserialized Output: ', deserializedData)
        return deserializedData


    def deserializeHelper(self, nodeList, indexs):
        if indexs[0] == len(nodeList):
            return None
        root = Node(int(nodeList[indexs[0]]), [])
        indexs[0] += 1
        childrenSize = int(nodeList[indexs[0]])
        indexs[0] += 1
        for index in range(childrenSize):
            root.children.append(self.deserializeHelper(nodeList, indexs))
            # print('root.children: ', root.children)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))