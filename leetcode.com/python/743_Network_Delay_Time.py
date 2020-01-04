#
import heapq
from collections import deque
from collections import defaultdict

"""
# Source: https://tinyurl.com/rmcr2xk. Uses simple DFS - Accepted
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
        if elapsedTimeSoFar >= distance[node]:
            return
        distance[node] = elapsedTimeSoFar
        for neighbour, time in sorted(graph[node]):
            self.DFS(graph, distance, neighbour, elapsedTimeSoFar + time)
"""


# """
# Source: https://tinyurl.com/vbetlaq. Uses simple BFS - Accepted
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
out =  sol.networkDelayTime(times, N, K)
print("RES: ", out)

