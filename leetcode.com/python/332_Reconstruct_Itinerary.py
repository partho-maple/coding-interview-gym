# Source: https://tinyurl.com/tsy24pl
from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        for source, destination in tickets:
            graph[source].append(destination)
        for source in graph.keys():
            graph[source].sort(reverse=True)
        stack = ["JFK",]
        result = []
        while stack:
            node = stack[-1]
            if node in graph and len(graph[node]) > 0:
                stack.append(graph[node].pop())
            else:
                result.append(stack.pop())
        return result[::-1]
