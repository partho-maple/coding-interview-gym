// DFS. Accepted. Time and Space: O(mn)
class Solution {
    func closedIsland(_ grid: [[Int]]) -> Int {
        guard grid.count > 2,
              grid[0].count > 2 else {
            return 0
        }
        var (grid, ilandCount) = (grid, 0)
        for row in 1..<grid.count - 1 {
            for col in 1..<grid[0].count - 1 {
                let value = grid[row][col]
                if value == 0 {
                    grid[row][col] = 2
                    ilandCount += dfs(&grid, row, col)
                }
            }
        }
        return ilandCount
    }
    
    @discardableResult
    func dfs(_ grid: inout [[Int]], _ row: Int, _ col: Int) -> Int {
        var results = [Int]()
        for (newRow, newCol) in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)] {
            if newRow >= 0 && newRow < grid.count && newCol >= 0 && newCol < grid[0].count {
                if newRow == 0 || newRow == grid.count - 1 || newCol == 0 || newCol == grid[0].count - 1 {
                    if grid[newRow][newCol] == 0 {
                        results.append(0)
                        grid[newRow][newCol] = 2
                        dfs(&grid, newRow, newCol)
                    }
                } else {
                    if grid[newRow][newCol] == 0 {
                        grid[newRow][newCol] = 2
                        results.append(dfs(&grid, newRow, newCol))
                    }
                }
            }
        }
        return results.allSatisfy { $0 == 1 } ? 1 : 0
    }
}

// BFS. Accepted. Time and Space: O(mn)
class Solution {
    func closedIsland(_ grid: [[Int]]) -> Int {
        guard grid.count > 2,
              grid[0].count > 2 else {
            return 0
        }
        var (grid, ilandCount) = (grid, 0)
        for row in 1..<grid.count - 1 {
            for col in 1..<grid[0].count - 1 {
                let value = grid[row][col]
                if value == 0 {
                    grid[row][col] = 2
                    ilandCount += bfs(&grid, row, col)
                }
            }
        }
        return ilandCount
    }
    
    @discardableResult
    func bfs(_ grid: inout [[Int]], _ row: Int, _ col: Int) -> Int {
        var isClosed = true
        var queue = [(Int, Int)]() // (row, col) of cells with value of 0
        queue.append((row, col))
        while !queue.isEmpty {
            let (currentRow, currentCol) = queue.removeFirst()
            for (newRow, newCol) in [(currentRow - 1, currentCol), (currentRow, currentCol + 1), (currentRow + 1, currentCol), (currentRow, currentCol - 1)] {
                if newRow >= 0 && newRow < grid.count && newCol >= 0 && newCol < grid[0].count {
                    if newRow == 0 || newRow == grid.count - 1 || newCol == 0 || newCol == grid[0].count - 1 {
                        if grid[newRow][newCol] == 0 {
                            isClosed = false
                            grid[newRow][newCol] = 2
                            queue.append((newRow, newCol))
                        }
                    } else {
                        if grid[newRow][newCol] == 0 {
                            grid[newRow][newCol] = 2
                            queue.append((newRow, newCol))
                        }
                    }
                }
            }
        }
        return isClosed ? 1 : 0
    }
}
