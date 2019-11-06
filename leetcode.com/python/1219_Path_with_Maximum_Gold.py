class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        totalGoldCollections = []
        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[0])):
                if grid[rowIdx][colIdx] != 0:
                    self.calculateGoldCollections(rowIdx, colIdx, 0, grid, totalGoldCollections)
        return max(totalGoldCollections)

    def calculateGoldCollections(self, rowIdx, colIdx, currentCollection, grid, totalGoldCollections):
        if rowIdx < 0 or rowIdx >= len(grid) or colIdx < 0 or colIdx >= len(grid[0]) or grid[rowIdx][colIdx] == 0:
            totalGoldCollections.append(currentCollection)
            return  # Backtrack
        currentCellGold = grid[rowIdx][colIdx]
        grid[rowIdx][colIdx] = 0  # To prevent revisiting the cell
        currentCollection += currentCellGold
        self.calculateGoldCollections(rowIdx - 1, colIdx, currentCollection, grid,
                                      totalGoldCollections)  # walk one step to the up
        self.calculateGoldCollections(rowIdx, colIdx - 1, currentCollection, grid,
                                      totalGoldCollections)  # walk one step to the left
        self.calculateGoldCollections(rowIdx + 1, colIdx, currentCollection, grid,
                                      totalGoldCollections)  # walk one step to the down
        self.calculateGoldCollections(rowIdx, colIdx + 1, currentCollection, grid,
                                      totalGoldCollections)  # walk one step to the right
        grid[rowIdx][colIdx] = currentCellGold  # Restoring the grid
        currentCollection -= currentCellGold  # recalculating collections




