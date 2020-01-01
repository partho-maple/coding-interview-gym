from collections import deque


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}
        for node in range(len(graph)):
            if node not in color and graph[node]:
                queue = deque([node])
                color[node] = 0
                while queue:
                    currentNode = queue.popleft()
                    for neighbour in graph[currentNode]:
                        if neighbour not in color:
                            queue.append(neighbour)
                            color[neighbour] = color[currentNode] ^ 1
                        elif color[neighbour] == color[currentNode]:
                            return False
        return True
