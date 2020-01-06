from collections import defaultdict
from collections import deque

"""
# Source: https://tinyurl.com/yx6ehrfu -  Using BFS
class Solution(object):
    def validTree(self, n, edges):
        if not edges:
            return True if n <= 1 else False
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)
        for edge in edges:
            node1, node2 = edge
            graph[node1].append(node2)
            graph[node2].append(node1)
        queue = deque([0])
        visited = [False] * n
        visited[0] = True
        while queue:
            currentNode = queue.popleft()
            for neighour in graph[currentNode]:
                if not visited[neighour]:
                    visited[neighour] = True
                    queue.append(neighour)
        return all(visited)
"""




# """
# Source: https://tinyurl.com/yx6ehrfu -  Using DFS
class Solution(object):
    def validTree(self, n, edges):
        if not edges:
            return True if n <= 1 else False
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)
        for edge in edges:
            node1, node2 = edge
            graph[node1].append(node2)
            graph[node2].append(node1)
        stack = [0]
        visited = [False] * n
        visited[0] = True
        while stack:
            currentNode = stack.pop()
            for neighour in graph[currentNode]:
                if not visited[neighour]:
                    visited[neighour] = True
                    stack.append(neighour)
        return all(visited)
# """




# """
# Source: https://tinyurl.com/yx6ehrfu -  Using Union FInd
class Solution(object):
    def validTree(self, n, edges):
        if not edges:
            return True if n <= 1 else False
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)
        for edge in edges:
            node1, node2 = edge
            graph[node1].append(node2)
            graph[node2].append(node1)
        stack = [0]
        visited = [False] * n
        visited[0] = True
        while stack:
            currentNode = stack.pop()
            for neighour in graph[currentNode]:
                if not visited[neighour]:
                    visited[neighour] = True
                    stack.append(neighour)
        return all(visited)
# """