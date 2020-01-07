from collections import defaultdict
from collections import deque
import heapq

# Using Kruskal's algorithm
class Solution(object):

    def __init__(self):
        self.parents = list()



    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]



    def union(self, node1, node2):
        parentOfNode1, parentOfNode2 = self.find(node1), self.find(node2)
        if parentOfNode1 != parentOfNode2:
            self.parents[parentOfNode1] = parentOfNode2
            return True
        return False



    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        self.parents = list(range(n + 1))
        cost, undone = 0, n

        totalPipes = []
        for i, w in enumerate(wells, 1):
            totalPipes.append([0,i,w])                            #   We can set 0 as water source that connected with each well which needs to be eventually unioned.

        totalPipes = totalPipes + pipes
        totalPipes = sorted(totalPipes, key=lambda x: x[2])

        for u, v, w in totalPipes:
            if self.union(u, v):
                cost += w
                undone -= 1
            if not undone:
                break
        return cost






sol = Solution()
n = 3
wells = [1,2,2]
pipes = [[1,2,1],[2,3,1]]
out = sol.minCostToSupplyWater(n, wells, pipes)
print("Res: ", out)




