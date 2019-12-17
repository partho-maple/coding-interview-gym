# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import defaultdict


# class Solution:

#     def distanceK(self, root, target, K):
#         """
#         :type root: TreeNode
#         :type target: TreeNode
#         :type K: int
#         :rtype: List[int]
#         """
#         graph = defaultdict(set)
#         visited = set()
#         res = [target.val]
#         self.dfs(root, target.val, graph)

#         for _ in range(K):
#             size, level = len(res), []

#             for _ in range(size):
#                 cur = res.pop()
#                 if cur not in visited:
#                     level += graph.get(cur, [])
#                     visited.add(cur)

#             res = level

#         return [val for val in res if val not in visited]


#     def dfs(self, root, target, graph):
#         if not root:
#             return

#         if root.left:
#             graph[root.val].add(root.left.val)
#             graph[root.left.val].add(root.val)
#             self.dfs(root.left, target, graph)

#         if root.right:
#             graph[root.val].add(root.right.val)
#             graph[root.right.val].add(root.val)
#             self.dfs(root.right, target, graph)


# Source:   https://tinyurl.com/t3ozct3 and https://tinyurl.com/tn4ncqy
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # Create the node to parent map and populate it
        nodeToParentMap = defaultdict(list)
        self.populateNodeToParentMap(root, None, nodeToParentMap)

        # Create the queue that we will use for the breadth first search.
        # Add the start node to the queue
        queue = [target, ]

        # The is an undirected graph now that we can go to and from nodes.
        # Before we could only go down the tree.
        # Therefore, we need a hashtable to keep track of nodes we have
        # visited so that we do not go back and revisit what has already
        # been processed and cause an infinite cycle
        visited = set()
        visited.add(target)

        # When our search starts, we are standing at distance 0
        currentDistance = 0
        while queue:

            # Is this the distance we want? If so, extract and return it
            if currentDistance == K:
                return self.extractLayerFromQueue(queue)

            # How many nodes do we have of that distance? Let's process all node in the distance.
            # This is Breadth First Search.
            nodeCountOfCurrentDistance = len(queue)
            for idx in range(nodeCountOfCurrentDistance):

                # Pull a node from the search queue, we are going to basically
                # use our current layer to populate the next layer of nodes
                # that we need to search in the next while loop iteration
                currentNode = queue.pop(0)

                # Has left been touched before?
                # No?
                #   1.) Add it to the seen hashtable
                #   2.) Add it to the search queue
                if currentNode.left and currentNode.left not in visited:
                    visited.add(currentNode.left)
                    queue.append(currentNode.left)

                # Has right been touched before?
                # No?
                #   1.) Add it to the seen hashtable
                #   2.) Add it to the search queue
                if currentNode.right and currentNode.right not in visited:
                    visited.add(currentNode.right)
                    queue.append(currentNode.right)

                # Has this node's parent been touched before?
                # No?
                #   1.) Add it to the seen hashtable
                #   2.) Add it to the search queue
                parentOfCurrentNode = nodeToParentMap[currentNode]
                if parentOfCurrentNode and parentOfCurrentNode not in visited:
                    visited.add(parentOfCurrentNode)
                    queue.append(parentOfCurrentNode)

            # Advance the layer for the next iteration
            currentDistance += 1
        return []

    # inorder DFS tree traversalto populate the dictionary.
    # When this recursion is done we will know all nodes' parents.
    # The tree then can be treated and searched like any other graph
    def populateNodeToParentMap(self, node, parent, nodeToParentMap):
        # We can't add a null node to the map, return
        if not node:
            return

        # Map the node to its parent
        nodeToParentMap[node] = parent

        # Go left and after that go right. The call that we make next
        # will have what we call 'root' now as the 'parent' value so
        # we can do the mapping in THAT call stack frame...and so on
        # and so on...
        self.populateNodeToParentMap(node.left, node, nodeToParentMap)
        self.populateNodeToParentMap(node.right, node, nodeToParentMap)

    def extractLayerFromQueue(self, queue):
        resultNodes = []
        for node in queue:
            resultNodes.append(node.val)
        return resultNodes
