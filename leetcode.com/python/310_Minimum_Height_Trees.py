from collections import deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 0:
            return []

        # with only one node, since its in-degrees will be 0, therefore, we need to handle it separately
        if n == 1:
            return [0]

        # a. Initialize the graph
        inDegree = {i: 0 for i in range(n)}                             # count of incoming edges
        graph = {i: [] for i in range(n)}                               # adjacency list graph

        # b. Build the graph
        for edge in edges:
            node1, node2 = edge[0], edge[1]

            # since this is an undirected graph, therefore, add a link for both the nodes
            graph[node1].append(node2)
            graph[node2].append(node1)

            # increment the in-degrees of both the nodes
            inDegree[node1] += 1
            inDegree[node2] += 1

        # c. Find all leaves i.e., all nodes with 0 in-degrees
        leaves = deque()
        for key in inDegree:
            if inDegree[key] == 1:
                leaves.append(key)

        # d. Remove leaves level by level and subtract each leave's children's in-degrees.
        # Repeat this until we are left with 1 or 2 nodes, which will be our answer.
        # Any node that has already been a leaf cannot be the root of a minimum height tree, because
        # its adjacent non-leaf node will always be a better candidate.
        totalNodes = n
        while totalNodes > 2:
            leavesSize = len(leaves)
            totalNodes -= leavesSize
            for i in range(0, leavesSize):
                vertex = leaves.popleft()
                # get the node's children to decrement their in-degrees
                for child in graph[vertex]:
                    inDegree[child] -= 1
                    if inDegree[child] == 1:
                        leaves.append(child)

        return list(leaves)

