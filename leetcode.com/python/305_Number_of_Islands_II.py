from collections import defaultdict

class Solution(object):

    # the number of islands using
    # Disjoint Set data structure.

    # Class to represent
    # Disjoint Set Data structure
    class DisjointUnionSets(object):

        def __init__(self, n):
            self.rank = [0] * n
            self.parent = [0] * n
            self.n = n
            self.makeSet()

        def makeSet(self):

            # Initially, all elements are in their
            # own set.
            for i in range(self.n):
                self.parent[i] = i

        # Finds the representative of the set that x is an element of
        def find(self, x):
            if (self.parent[x] != x):
                # if x is not the parent of itself,
                # then x is not the representative of
                # its set.
                # so we recursively call Find on its parent
                # and move i's node directly under the
                # representative of this set
                return self.find(self.parent[x])
            return x

        # Unites the set that includes x and the set that includes y
        def Union(self, x, y):

            # Find the representatives(or the root nodes)
            # for x an y
            xRoot = self.find(x)
            yRoot = self.find(y)

            # Elements are in the same set,
            # no need to unite anything.
            if xRoot == yRoot:
                return

            # If x's rank is less than y's rank
            # Then move x under y so that depth of tree
            # remains less
            if self.rank[xRoot] < self.rank[yRoot]:
                self.parent[xRoot] = yRoot

                # Else if y's rank is less than x's rank
            # Then move y under x so that depth of tree
            # remains less
            elif self.rank[yRoot] < self.rank[xRoot]:
                self.parent[yRoot] = xRoot
            else:

                # Else if their ranks are the same
                # Then move y under x (doesn't matter
                # which one goes where)
                self.parent[yRoot] = xRoot

                # And increment the result tree's
                # rank by 1
                self.rank[xRoot] = self.rank[xRoot] + 1

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        rowCount, colCount, currentIlandCount = m, n, 0
        grid = [[0 for _ in range(colCount)] for _ in range(rowCount)]
        numOfIlands = []
        unionFind = self.DisjointUnionSets(rowCount * colCount)

        for position in positions:
            rowIdx, colIdx = position[0], position[1]
            if grid[rowIdx][colIdx] == "1":         # already unified
                numOfIlands.append(currentIlandCount)
                continue
            grid[rowIdx][colIdx] = "1"
            currentIlandCount += 1
            currentIndex = rowIdx * colCount + colIdx
            neighoursParentDict = defaultdict(int)

            for rowIdxOfNeighbour, colIdxOfNeighbour in ((rowIdx - 1, colIdx), (rowIdx + 1, colIdx), (rowIdx, colIdx - 1), (rowIdx, colIdx + 1)):
                if 0 <= rowIdxOfNeighbour <= rowCount - 1 and 0 <= colIdxOfNeighbour <= colCount - 1 and grid[rowIdxOfNeighbour][colIdxOfNeighbour] == "1":
                    neighborIndex = rowIdxOfNeighbour * colCount + colIdxOfNeighbour
                    neighborsParent = unionFind.find(neighborIndex)
                    currentParent = unionFind.find(currentIndex)
                    if neighborsParent not in neighoursParentDict and neighborsParent != currentParent:
                        unionFind.Union(currentIndex, neighborIndex)
                        currentIlandCount -= 1
                        neighoursParentDict[neighborsParent] = neighborIndex

            currentIlandCount = currentIlandCount if currentIlandCount > 1 else 1
            numOfIlands.append(currentIlandCount)

        return numOfIlands








# SOURCE:   https://tinyurl.com/qohtl3m
class UnionFind(object):
    def __init__(self):
        self.parents = {}
        self.set_count = 0

    def make_set(self, x):
        self.parents[x] = x
        self.set_count += 1

    def find(self, x):
        if x not in self.parents:
            self.make_set(x)
            return x
        elif self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        if x_set != y_set:
            self.parents[x_set] = y_set
            self.set_count -= 1


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        island_counts = []
        uf = UnionFind()
        rowCount, colCount = m, n
        for rowIdx, colIdx in positions:
            index = rowIdx * colCount + colIdx
            uf.make_set(index)
            for rowIdxOfNeighbour, colIdxOfNeighbour in ((rowIdx - 1, colIdx), (rowIdx + 1, colIdx), (rowIdx, colIdx - 1), (rowIdx, colIdx + 1)):
                if 0 <= rowIdxOfNeighbour <= rowCount - 1 and 0 <= colIdxOfNeighbour <= colCount - 1:
                    neighbor_index = rowIdxOfNeighbour * colCount + colIdxOfNeighbour
                    if neighbor_index in uf.parents:
                        uf.union(index, neighbor_index)
            island_counts.append(uf.set_count)
        return island_counts











sol = Solution()

# m = 2
# n = 2
# positions = [[0,0],[1,1],[0,1]]
# Expected: [1,2,1]

m = 3
n = 3
positions = [[0,0],[0,1],[1,2],[2,1]]
# Expected: [1,1,2,3]

# m = 3
# n = 3
# positions = [[0,0],[0,1],[1,2],[1,2]]
# Expected: [1,1,2,2]

# Getting wrong answer on this test case
# m = 21
# n = 71
# positions = [[19,28],[14,38],[15,44],[17,12],[6,19],[11,69],[2,30],[7,43],[19,6],[7,29],[10,21],[17,55],[20,66],[12,28],[11,64],[12,52],[18,15],[2,52],[10,20],[0,50],[16,5],[17,25],[12,67],[6,45],[13,17],[5,55],[10,42],[20,17],[3,26],[20,61],[14,10],[9,1],[9,69],[6,29],[11,53],[3,66],[4,45],[12,65],[11,35],[5,67],[18,35],[2,57],[12,12],[13,53],[9,65],[13,0],[3,18],[13,39],[5,54],[20,43],[19,29],[17,37],[17,45],[3,38],[2,61],[2,65],[3,21],[5,40],[10,4],[12,36],[2,8],[3,33],[15,4],[13,35],[0,45],[20,29],[10,66],[19,7],[0,46],[19,11],[10,22],[19,0],[0,9],[2,20],[16,64],[10,37],[16,49],[4,20],[20,68],[10,38],[17,59],[15,54],[17,60],[19,18],[0,60],[9,62],[3,69],[10,44],[15,2],[14,44],[17,0],[18,42],[17,28],[11,10],[11,42],[11,67],[0,32],[8,0],[17,6],[7,26],[17,65],[17,66],[7,38],[8,17],[7,60],[0,16],[7,59],[18,8],[16,63],[7,0],[11,46],[0,7],[6,4],[2,63],[8,56],[18,18],[12,70],[2,15],[14,65],[13,52],[11,0],[10,48],[7,8],[11,44],[0,35],[4,64],[6,36],[16,17],[7,34],[1,33],[11,60],[17,11],[4,58],[4,9],[18,7],[15,40],[11,24],[17,3],[7,9],[1,38],[1,14],[15,21],[14,68],[14,69],[16,40],[5,60],[18,46],[15,51],[7,65],[1,34],[15,55],[19,63],[5,35],[20,9],[13,1],[20,69],[19,67],[17,44],[12,44],[10,49],[12,43],[14,21],[18,11],[11,9],[4,56],[6,70],[8,54],[1,55],[17,47],[18,38],[3,31],[16,37],[13,7],[15,6],[18,33],[4,60],[17,40],[7,3],[3,32],[13,41],[5,62],[17,4],[20,5],[15,32],[19,31],[8,69],[19,58],[3,35],[6,64],[0,37],[15,56],[6,46],[4,42],[4,51],[2,7],[7,13],[20,47],[10,29],[12,18],[20,52],[5,5],[12,34],[1,57],[7,32],[3,58],[14,29],[2,32],[2,46],[14,5],[3,9],[19,68],[18,16],[19,2],[6,23],[20,3],[10,69],[9,0],[0,13],[20,38],[6,14],[0,21],[6,50],[2,5],[1,20],[5,20],[1,5],[10,0],[7,6],[15,13],[8,21],[7,14],[9,9],[19,8],[13,25],[5,30],[1,16],[18,19],[16,44],[4,5],[15,37],[20,14],[20,8],[5,23],[13,44],[17,56],[13,62],[2,18],[1,58],[17,2],[20,40],[8,9],[8,52],[6,24],[19,65],[7,48],[20,51],[2,21],[7,39],[11,27],[7,22],[12,6],[19,12],[12,66],[0,55],[20,62],[11,20],[2,35],[2,0],[6,7],[5,41],[9,37],[8,44],[16,15],[9,48],[18,54],[19,52],[19,24],[19,46],[5,0],[19,50],[2,37],[18,31],[6,20],[4,59],[5,39],[9,38],[19,51],[3,67],[11,33],[7,57],[13,47],[20,64],[8,24],[13,69],[4,11],[4,46],[13,32],[18,3],[20,54],[18,17],[7,5],[15,12],[12,7],[6,11],[5,4],[17,26],[7,12],[12,68],[8,45],[8,2],[15,34],[12,20],[1,26],[6,54],[19,16],[0,17],[9,13],[4,65],[12,58],[11,52],[8,32],[18,32],[11,50],[9,50],[17,13],[11,17],[16,53],[18,26],[2,42],[14,58],[0,23],[19,44],[9,39],[15,47],[11,70],[10,35],[8,41],[15,39],[20,50],[2,50],[17,39],[1,28],[7,63],[16,61],[15,58],[19,17],[11,40],[20,46],[12,41],[6,32],[2,67],[4,52],[14,24],[0,43],[17,34],[6,56],[2,53],[1,69],[0,11],[16,48],[1,47],[14,12],[7,23],[8,37],[17,18],[7,27],[7,2],[10,63],[13,6],[3,23],[12,8],[1,52],[11,30],[9,57],[16,57],[9,58],[4,38],[18,36],[10,17],[20,24],[13,64],[18,37],[4,21],[17,33],[2,33],[15,10],[8,40],[14,52],[19,1],[2,45],[11,55],[3,40],[8,31],[20,57],[6,33],[6,22],[6,28],[2,11],[4,15],[4,31],[16,26],[9,27],[10,61],[5,52],[3,68],[0,19],[13,40],[0,52],[18,22],[1,24],[13,29],[12,33],[16,58],[19,66],[6,62],[18,40],[17,58],[2,34],[15,63],[8,23],[14,50],[20,16],[6,9],[8,1],[3,0],[20,10],[15,23],[1,0],[13,4],[8,25],[10,13],[12,9],[18,39],[3,24],[20,63],[16,39],[7,36],[15,65],[13,10],[19,20],[3,54],[12,35],[17,49],[17,31],[14,48],[18,65],[2,44],[9,51],[17,64],[16,36],[7,10],[5,9],[12,13],[6,59],[13,21],[8,14],[10,67],[20,56],[6,53],[18,25],[14,39],[8,70],[10,27],[0,48],[0,36],[12,56],[3,28],[15,14]]

out = sol.numIslands2(m, n, positions)
print("Res: ", out)
