import heapq
from collections import deque
from collections import defaultdict

# """
# Source: https://tinyurl.com/rmcr2xk. Uses simple DFS - Time Limit Exceeded
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        distance = {node: float("inf") for node in range(1, N + 1)}
        self.DFS(graph, distance, K, 0)
        totalTime = max(distance.values())
        return totalTime if totalTime < float("inf") else -1

    def DFS(self, graph, distance, node, elapsedTimeSoFar):
        if elapsedTimeSoFar >= distance[node]:  # Here we are essentially checking if our existing/already calculated disstance is grater than out current culculated time. If our current path is greated than already traverssed path then this path is't going to give us any better solution. so we leave this path.
            return
        distance[node] = elapsedTimeSoFar
        for neighbour, time in sorted(graph[node]):
            self.DFS(graph, distance, neighbour, elapsedTimeSoFar + time)
# """


# """
# Source: https://tinyurl.com/vbetlaq. Uses simple BFS - Accepted. Here BFS if preferable over DFS
class Solution:
    def networkDelayTime(self, times, N, K):
        elapsedTime, graph, queue = [0] + [float("inf")] * N, defaultdict(list), deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while queue:
            time, node = queue.popleft()
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    queue.append((time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1
# """



# """
# Source: https://tinyurl.com/vbetlaq. Uses Heap: Dijkstra algorithm - Accepted
class Solution:
    def networkDelayTime(self, times, N, K):
        elapsedTime, graph, heap = [0] + [float("inf")] * N, defaultdict(list), [(0, K)]
        for u, v, w in times:
            graph[u].append((v, w))
        while heap:
            time, node = heapq.heappop()
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    heapq.heappush(heap, (time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1
# """





# """
# Belman Ford - Accepted
class Solution:
    def networkDelayTime(self, times, N, K):
        elapsedTime, graph, queue = [0] + [float("inf")] * N, defaultdict(list), deque([(0, K)])
        elapsedTime[K] = 0
        for u, v, w in times:
            graph[u].append((v, w))
        while queue:
            time, node = queue.popleft()
            for neighbour in graph[node]:
                v, w = neighbour
                if time + w < elapsedTime[v]:
                    elapsedTime[v] = time + w
                    queue.append((time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1
# """





# """
# Source: https://tinyurl.com/roq3udj    Floyd Warshall - Accepted
class Solution:
    def networkDelayTime(self, times, N, K):
        elapsedTimeMatrix = [[float("inf") for _ in range(N)] for _ in range(N)]
        for u, v, w in times:
            elapsedTimeMatrix[u - 1][v - 1] = w
        for i in range(N):                      #   Assigning 0 to the diagonal cells
            elapsedTimeMatrix[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    elapsedTimeMatrix[i][j] = min(elapsedTimeMatrix[i][j], elapsedTimeMatrix[i][k] + elapsedTimeMatrix[k][j])
        mx = max(elapsedTimeMatrix[K - 1])
        return mx if mx < float("inf") else -1
# """



sol = Solution()
# times = [[2,1,1],[2,3,1],[3,4,1]]
# N = 4
# K = 2

# times = [[1,2,1],[2,1,3]]
# N = 2
# K = 2

times = [[1,2,1],[2,3,2],[1,3,2]]
N = 3
K = 1
out = sol.networkDelayTime(times, N, K)
print("RES: ", out)

