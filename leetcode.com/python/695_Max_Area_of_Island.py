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
        sizes.sort(reverse= False)
        if not sizes:
            return 0
        else:
            return sizes[-1]


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
            if grid[i][j] == 0:
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










# My Own solution during MOCK
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sizes = [0]
        visited = [[False for _ in row] for row in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 1:
                    self.traverseNode(i, j, grid, visited, sizes)
        sizes.sort()
        return sizes[-1]

    def traverseNode(self, row, col, grid, visited, sizes):
        nodesStack = [[row, col]]
        currentSize = 0
        while nodesStack:
            i, j = nodesStack.pop()
            if visited[i][j] == False:
                visited[i][j] = True
                currentSize += 1
                unvisitedValidNeighbours = self.getUnvisitedValidNeighbours(i, j, grid, visited)
                nodesStack.extend(unvisitedValidNeighbours)
        sizes.append(currentSize)

    def getUnvisitedValidNeighbours(self, row, col, grid, visited):
        neighbours = []
        if row > 0 and grid[row - 1][col] == 1 and not visited[row - 1][col]:
            neighbours.append([row - 1, col])
        if row < len(grid) - 1 and grid[row + 1][col] and not visited[row + 1][col]:
            neighbours.append([row + 1, col])
        if col > 0 and grid[row][col - 1] and not visited[row][col - 1]:
            neighbours.append([row, col - 1])
        if col < len(grid[0]) - 1 and grid[row][col + 1] and not visited[row][col + 1]:
            neighbours.append([row, col + 1])
        return neighbours








# Driver code
sol = Solution()
# grid = [[1,1,0,0,0],
#         [1,1,0,0,0],
#         [0,0,0,1,1],
#         [0,0,0,1,1]]
grid = [[0]]
numOfIlands = sol.numIslands(grid)
print("Max Area of Iands: ", numOfIlands)