class Solution(object):

    # Backtrackng approach. Getting TLE. fix it.
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        allDistances = []
        self.calculateDistances(workers, bikes, allDistances, 0)
        print(allDistances)
        return min(allDistances)


    def calculateDistances(self, workers, bikes, allDistances, runningDistance):
        if len(workers) == 0:
            allDistances.append(runningDistance)
            return
        for i in range(len(workers)):
            for j in range(len(bikes)):
                manhuttonDistance = self.getManhattanDistance(workers[i], bikes[j])
                runningDistance += manhuttonDistance
                worker = workers[i]
                bike = bikes[j]
                workers.pop(i)
                bikes.pop(j)
                self.calculateDistances(workers, bikes, allDistances, runningDistance)
                runningDistance -= manhuttonDistance
                workers.insert(i, worker)
                bikes.insert(j, bike)


    def getManhattanDistance(self, worker, bike):
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])




sol = Solution()
workers = [[0, 0], [1, 1], [2, 0]]
bikes = [[1, 0], [2, 2], [2, 1]]
# workers = [[0,0],[1,0],[2,0],[3,0],[4,0]]
# bikes = [[0,999],[1,999],[2,999],[3,999],[4,999],[5,999],[6,999],[7,999],[8,999]]
output = sol.assignBikes(workers, bikes)
print("Res: ", output)