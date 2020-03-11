# Approach 1: Using Union Find.   Source: https://tinyurl.com/tgzexdk
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


    # Returns number of islands in a[][]
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rowCount = len(grid)
        colCount = len(grid[0])

        dus = self.DisjointUnionSets(rowCount * colCount)

        # The following loop checks for its neighbours
        # and unites the indexes if both are 1.
        for rowIdx in range(0, rowCount):
            for colIdx in range(0, colCount):

                # If cell is 0, nothing to do
                if grid[rowIdx][colIdx] == "0":
                    continue

                # Check all 4 neighbours and do a Union
                # with neighbour's set if neighbour is
                # also 1
                if rowIdx + 1 < rowCount and grid[rowIdx + 1][colIdx] == "1":
                    dus.Union(rowIdx * (colCount) + colIdx, (rowIdx + 1) * (colCount) + colIdx)

                if rowIdx - 1 >= 0 and grid[rowIdx - 1][colIdx] == "1":
                    dus.Union(rowIdx * (colCount) + colIdx, (rowIdx - 1) * (colCount) + colIdx)

                if colIdx + 1 < colCount and grid[rowIdx][colIdx + 1] == "1":
                    dus.Union(rowIdx * (colCount) + colIdx, (rowIdx) * (colCount) + colIdx + 1)

                if colIdx - 1 >= 0 and grid[rowIdx][colIdx - 1] == "1":
                    dus.Union(rowIdx * (colCount) + colIdx, (rowIdx) * (colCount) + colIdx - 1)

        # Array to note down frequency of each set
        frequencyArray = [0] * (rowCount * colCount)
        numberOfIslands = 0
        for rowIdx in range(rowCount):
            for colIdx in range(colCount):
                gridVal = grid[rowIdx][colIdx]
                if gridVal == "1":
                    x = dus.find(rowIdx * colCount + colIdx)

                    # If frequency of set is 0,
                    # increment numberOfIslands
                    if frequencyArray[x] == 0:
                        numberOfIslands += 1
                        frequencyArray[x] += 1
                    else:
                        frequencyArray[x] += 1
        return numberOfIslands








# Approach 2: Using DFS - Accepted
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        sizes = []
        visited = [[False for value in row] for row in grid]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j]:
                    continue
                else:
                    self.traverseNode(i, j, grid, visited, sizes)
        return len(sizes)


    def traverseNode(self, i, j, grid, visited, sizes):
        currentRiverSize = 0
        nodesToExplore = [[i, j]]
        while len(nodesToExplore):
            currentNode = nodesToExplore.pop()
            i = currentNode[0]
            j = currentNode[1]
            if visited[i][j]:
                continue
            visited[i][j] = True
            if grid[i][j] == "0":
                continue
            currentRiverSize += 1
            unvisitedNeighbours = self.getUnvisitedNeighbour(i, j, grid, visited)
            for neighbour in unvisitedNeighbours:
                nodesToExplore.append(neighbour)
        if currentRiverSize > 0:
            sizes.append(currentRiverSize)



    def getUnvisitedNeighbour(self, i, j, grid, visited):
        unvisitedNeighbours = []
        if i > 0 and not visited[i - 1][j]:
            unvisitedNeighbours.append([i - 1, j])
        if i < len(grid) - 1 and not visited[i + 1][j]:
            unvisitedNeighbours.append([i + 1, j])
        if j > 0 and not visited[i][j - 1]:
            unvisitedNeighbours.append([i, j - 1])
        if j < len(grid[0]) - 1 and not visited[i][j + 1]:
            unvisitedNeighbours.append([i, j + 1])
        return unvisitedNeighbours





# Driver code
sol = Solution()
grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]  # It's output is 3

# grid = [["1","1","1","1","0"],
#         ["1","1","0","1","0"],
#         ["1","1","0","0","0"],
#         ["0","0","0","0","0"]]  # It's output is 1
numOfIlands = sol.numIslands(grid)
print("Number of Iands: ", numOfIlands)