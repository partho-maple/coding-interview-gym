from collections import defaultdict


class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        gardenGraph = defaultdict(list)
        planted = defaultdict(int)
        for path in paths:
            g1, g2 = path
            gardenGraph[g1].append(g2)
            gardenGraph[g2].append(g1)
        for garden in gardenGraph:
            if planted[garden] <= 0:
                usedFlowers = []
                for neighbour in gardenGraph[garden]:
                    usedFlowers.append(planted[neighbour])
                for flowers in range(1, 5):
                    if flowers not in usedFlowers:
                        planted[garden] = flowers
        flowers = []
        for garden in range(1, N + 1):
            if garden in planted:
                flowers.append(planted[garden])
            else:
                flowers.append(1)
        return flowers
