# Source: https://tinyurl.com/yc2tzb4k
import collections


class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        for connection in connections:
            x, y = connection
            graph[x].append(y)
            graph[y].append(x)

        criticalConnections = set(map(tuple, map(sorted, connections)))
        serverRank = [-2] * n
        self.dfsServerSearch(0, 0, graph, serverRank, criticalConnections,
                             n)  # since this is a connected graph, we don't have to loop over all nodes.
        return list(criticalConnections)

    def dfsServerSearch(self, serverNode, depth, graph, serverRank, criticalConnections, n):
        if serverRank[serverNode] >= 0:
            return serverRank[serverNode]  # # visiting (0<=serverRank<n), or visited (serverRank=n)
        serverRank[serverNode] = depth
        minBackDepth = n
        for neighbour in graph[serverNode]:
            if serverRank[neighbour] == depth - 1:
                continue  # don't immmediately go back to parent. that's why i didn't choose -1 as the special value, in case depth==0.
            backDepth = self.dfsServerSearch(neighbour, depth + 1, graph, serverRank, criticalConnections, n)
            if backDepth <= depth:
                criticalConnections.discard(tuple(sorted((serverNode, neighbour))))
            minBackDepth = min(minBackDepth, backDepth)
        return minBackDepth
