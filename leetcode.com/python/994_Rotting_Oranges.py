from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visitedSet = set()
        unvisitedSet = set()
        queue = deque()
        depth = 0
        rowCount, colCount = len(grid), len(grid[0])
        totalOranges = 0
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == 2:
                    queue.append((i, j, 2))
                    unvisitedSet.add((i, j))
                    totalOranges += 1
                elif grid[i][j] == 1:
                    totalOranges += 1

        if totalOranges == 0:
            return 0

        while queue:
            i, j, val = queue[0]
            levelSize = len(queue)
            if val != 2:
                depth += 1
            while levelSize > 0:
                i, j, val = queue.popleft()
                if (i, j) not in visitedSet:
                    visitedSet.add((i, j))
                    unvisitedSet.discard((i, j))
                    neighbours = self.getFrreshNeighbours(i, j, grid, visitedSet)
                    for neighbour in neighbours:
                        r, c, val = neighbour
                        if (r, c) not in unvisitedSet:
                            queue.append(neighbour)
                            unvisitedSet.add((r, c))
                levelSize -= 1
        return depth if totalOranges == len(visitedSet) else -1

    def getFrreshNeighbours(self, r, c, grid, visitedSet):
        neighbours = []
        if r > 0 and grid[r - 1][c] == 1 and (r - 1, c) not in visitedSet:
            neighbours.append((r - 1, c, 1))
        if r < len(grid) - 1 and grid[r + 1][c] == 1 and (r + 1, c) not in visitedSet:
            neighbours.append((r + 1, c, 1))
        if c > 0 and grid[r][c - 1] == 1 and (r, c - 1) not in visitedSet:
            neighbours.append((r, c - 1, 1))
        if c < len(grid[0]) - 1 and grid[r][c + 1] == 1 and (r, c + 1) not in visitedSet:
            neighbours.append((r, c + 1, 1))
        return neighbours