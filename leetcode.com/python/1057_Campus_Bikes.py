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

        # First step: claculate distances of all (worker, bike) pairs and make a dictionary using them. Distances are the keys in this dictionay.
        # The dictionary will look like this: distances = {dist_val1: [[w1,b1],[w2,b3]], dist_val2: [[w0,b1],[w1,b2]], ...}
        for i in range(len(workers)):
            for j in range(len(bikes)):
                distances[self.getManhattanDistance(bikes[j], workers[i])].append([i, j])

        # Second, start from the minimum value in the dictionary and loop through the (worker, bike) pairs for that distance,
        # if the bike has not been assigned yet and the worker doesn't have a bike yet, assign the bike to that worker.
        # Since we created this dictionary, going through workers and bikes in ascending order, we don't need to sort the list of each distance[k].
        # If n is the total number of pairs between workers and bikes, making the dictionary if of O(n).
        # Also, worst case scenario, each entry in the dictionary belongs to one pair of worker and bike which makes filling ans to be of O(n) and the overall solution is of O(n).
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