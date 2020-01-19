# Backtracking with memoization - tle
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        minDistances = float("inf")
        usedBikes = [False] * (len(bikes))
        minDistances = self.calculateDistancesDFS(workers, 0, bikes, usedBikes, minDistances, 0)
        return minDistances

    def calculateDistancesDFS(self, workers, workerIdx, bikes, usedBikes, minDistances, runningDistance):
        if len(workers) == workerIdx:
            minDistances = min(minDistances, runningDistance)
            return minDistances
        if runningDistance >= minDistances:
            return minDistances
        for i in range(len(bikes)):
            if not usedBikes[i]:
                manhuttonDistance = self.getManhattanDistance(workers[workerIdx], bikes[i])
                runningDistance += manhuttonDistance
                usedBikes[i] = True
                minDistances = self.calculateDistancesDFS(workers, workerIdx + 1, bikes, usedBikes, minDistances, runningDistance)
                runningDistance -= manhuttonDistance
                usedBikes[i] = False
        return minDistances

    def getManhattanDistance(self, worker, bike):
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])











import heapq
from collections import defaultdict

# Source:  https://tinyurl.com/r4wtfbo   Accepted
# Augmented graph:
# vertex: (worker i, chosen bikes).
# edge: mahatan distance.
# Apply Dijkstra.

class Solution:
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """

        # each node int priority queue (cost, number of assigned workers, bikes status)
        pq = [(0, 0, '0' * len(bikes))]

        # optimal cost amongst all paths to reach a node
        optimal = defaultdict(lambda: float('inf'))

        while pq:
            cost, i, bike_status = heapq.heappop(pq)

            # early stopping with termination condition
            if i == len(workers):
                return cost

                # generate successors. The next worker to be assigned is at index i
            for j, b in enumerate(bikes):
                if bike_status[j] != '1':
                    new_cost = cost + self.manhattan(workers[i], b)
                    new_bike_status = bike_status[:j] + '1' + bike_status[j + 1:]

                    # update optimal cost if a new successor appears with lower cost to the same node
                    if new_cost < optimal[(i + 1, new_bike_status)]:
                        optimal[(i + 1, new_bike_status)] = new_cost
                        heapq.heappush(pq, (new_cost, i + 1, new_bike_status))

        return -1

    def manhattan(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])


sol = Solution()
workers = [[0, 0], [1, 1], [2, 0]]
bikes = [[1, 0], [2, 2], [2, 1]]
# workers = [[0,0],[1,0],[2,0],[3,0],[4,0]]
# bikes = [[0,999],[1,999],[2,999],[3,999],[4,999],[5,999],[6,999],[7,999],[8,999]]
output = sol.assignBikes(workers, bikes)
print("Res: ", output)