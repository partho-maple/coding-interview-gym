# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

from collections import defaultdict

class Graph:


    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # a function used by DFS
    def dfs_utils(self, v, visited):
        visited[v] = True
        print(v)

        # recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] is False:
                self.dfs_utils(i, visited)

    def dfs(self, v):
        visited = [False]*(len(self.graph))
        self.dfs_utils(v, visited)



# Driver code. create graph
g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.dfs(2)
