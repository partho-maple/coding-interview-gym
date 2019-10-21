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
        ["0","0","0","1","1"]]
numOfIlands = sol.numIslands(grid)
print("Number of Iands: ", numOfIlands)