
# Approach 1: BFS. SOURCE: https://tinyurl.com/v4mlv9o
from collections import deque
from collections import defaultdict

class Solution(object):

    def buildGraph(self, equations, values, graph):
        for vertices, edgeWeight in zip(equations, values):
            vertex1, vertex2 = vertices
            graph[vertex1].append((vertex2, edgeWeight))
            graph[vertex2].append((vertex1, 1 / edgeWeight))


    def findPath(self, query, graph):
        startVertex, endVertex = query
        if startVertex not in graph or endVertex not in graph:
            return -1.0
        queue = deque([(startVertex, 1.0)])
        visitedVertices = set()
        while queue:
            currentVertex, currentProduct = queue.popleft()
            if currentVertex == endVertex:
                return currentProduct
            visitedVertices.add(currentVertex)
            for neighbourVertex, edgeWeight in graph[currentVertex]:
                if neighbourVertex not in visitedVertices:
                    queue.append((neighbourVertex, currentProduct * edgeWeight))
        return -1.0


    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)
        self.buildGraph(equations, values, graph)
        return [self.findPath(querie, graph) for querie in queries]

