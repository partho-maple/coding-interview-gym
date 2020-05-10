class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        distinctIlandSet = set()
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    currentIlanndPosition = []
                    self.numDistinctIslandsDFSHelper(grid, currentIlanndPosition, row, col, 0, 0)
                    distinctIlandSet.add(tuple(currentIlanndPosition))
        return len(distinctIlandSet)

    def numDistinctIslandsDFSHelper(self, grid, currentIlanndPosition, row, col, referrenceRowPos, referrenceColPos):
        grid[row][col] = -1  # marking this cell as visited
        currentIlanndPosition.append((referrenceRowPos, referrenceColPos))
        neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for neighbour in neighbours:
            dr, dc = neighbour
            nextR, nextC = row + dr, col + dc
            nextReferrenceRowPos, nextReferrenceColPos = referrenceRowPos + dr, referrenceColPos + dc
            if 0 <= nextR < len(grid) and 0 <= nextC < len(grid[0]) and grid[nextR][nextC] == 1:
                self.numDistinctIslandsDFSHelper(grid, currentIlanndPosition, nextR, nextC, nextReferrenceRowPos,
                                                 nextReferrenceColPos)

