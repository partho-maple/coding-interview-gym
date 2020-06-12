class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeterCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    perimeterCount += 4
                    neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    for neighbour in neighbours:
                        dR, dC = neighbour
                        newR, newC = row + dR, col + dC
                        if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == 1:
                            perimeterCount -= 1

        return perimeterCount
