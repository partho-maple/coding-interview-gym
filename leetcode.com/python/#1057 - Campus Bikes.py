import collections


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        ans = [-1] * len(workers)
        distances = collections.defaultdict(list)
        assignedBikesSets = set()

        for i in range(len(workers)):
            for j in range(len(bikes)):
                distances[self.getManhattanDistance(bikes[j], workers[i])].append([i, j])

        for key in sorted(distances.keys()):
            for i in range(len(distances[key])):
                if ans[distances[key][i][0]] == -1 and distances[key][i][1] not in assignedBikesSets:
                    ans[distances[key][i][0]] = distances[key][i][1]
                    assignedBikesSets.add(distances[key][i][1])

        return ans


    def getManhattanDistance(self, bike, worker):
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])




sol = Solution()
workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]
output = sol.assignBikes(workers, bikes)
print('Res: ', output)