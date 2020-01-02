"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

# Official Solution - DFS:    https://tinyurl.com/usxjk49
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visitedNodes = {}
        clonedNode = self.cloneGraphHelper(node, visitedNodes)
        return clonedNode

    def cloneGraphHelper(self, node, visitedNodes):
        if not node:
            return node
        if node in visitedNodes:
            return visitedNodes[node]
        clonedNode = Node(node.val, [])
        visitedNodes[node] = clonedNode
        if node.neighbors:
            clonedNeighbor = []
            for neighbor in node.neighbors:
                clonedNeighbor.append(self.cloneGraphHelper(neighbor, visitedNodes))
            clonedNode.neighbors = list(clonedNeighbor)
        return clonedNode




from collections import deque
# Official Solution - BFS:    https://tinyurl.com/usxjk49
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        queue = deque([node])
        visitedNodes = {node: Node(node.val, [])}
        while queue:
            currentNode = queue.popleft()
            for neighbour in currentNode.neighbors:
                if neighbour not in visitedNodes:
                    clonedNode = Node(neighbour.val, [])
                    visitedNodes[neighbour] = clonedNode
                    queue.append(neighbour)
                visitedNodes[currentNode].neighbors.append(visitedNodes[neighbour])
        return visitedNodes[node]

