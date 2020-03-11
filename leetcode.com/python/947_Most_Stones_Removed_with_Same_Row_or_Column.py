# Source: https://tinyurl.com/sxyzxkr
# Approach 1: DFS
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        if len(stones) < 2:
            return 0
        disJointSetCount, visited = 0, set()
        for x, y in stones:
            if (x, y) not in visited:
                self.DFS(stones, visited, x, y)
                disJointSetCount += 1
        return len(stones) - disJointSetCount

    def DFS(self, stones, visited, x, y):
        if (x, y) not in visited:
            visited.add((x, y))
            for nextX, nextY in stones:
                if x == nextX:
                    self.DFS(stones, visited, x, nextY)
                if y == nextY:
                    self.DFS(stones, visited, nextX, y)




# Approach 2: Union Find
class Solution(object):

    class DisjointUnionSets(object):
        def __init__(self, numberOfSets):
            self.rank = [0 for _ in range(numberOfSets)]
            self.parent = [i for i in range(numberOfSets)]
            self.numberOfSets = numberOfSets

        def find(self, setElement):
            parentOfSetElement = self.parent[setElement]
            if parentOfSetElement != setElement:
                return self.find(parentOfSetElement)
            return parentOfSetElement

        def union(self, elementA, elementB):
            parentA, parentB = self.find(elementA), self.find(elementB)
            if parentA == parentB:
                return
            if self.rank[parentA] >= self.rank[parentB]:
                self.parent[parentB] = parentA
                self.rank[parentA] += self.rank[parentB]
            else:
                self.parent[parentA] = parentB
                self.parent[parentB] += self[parentA]
            self.numberOfSets -= 1

    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        numberOfStones = len(stones)
        disjointSet = self.DisjointUnionSets(numberOfStones)
        for i in range(len(numberOfStones)):
            for j in range(i + 1, numberOfStones):
                if (stones[i][1] == stones[j][1]) or (stones[i][0] == stones[j][0]):
                    disjointSet.union(i, j)

        return numberOfStones - disjointSet.numberOfSets
