// Simple DFS without memoization. TLE
class Solution {
    func shortestPath(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count, n = grid[0].count
        var minSteps = Int.max, visitedGrid = Array(repeating: Array(repeating: -1, count: n), count: m)
        shortestPathDFSHelper(grid, k, k, 0, 0, 0, &minSteps, &visitedGrid)
        return minSteps == Int.max ? -1 : minSteps
    }

    func shortestPathDFSHelper(
        _ grid: [[Int]],
        _ k: Int,
        _ remainingK: Int,
        _ startRowIdx: Int,
        _ startColIdx: Int,
        _ currentSteps: Int,
        _ minSteps: inout Int,
        _ visitedGrid: inout [[Int]]
    ) {
        let m = grid.count, n = grid[0].count
        if remainingK < 0 {
            return
        }
        if startRowIdx == m - 1 && startColIdx == n - 1 {
            minSteps = min(minSteps, currentSteps)
            return
        }

        for (r, c) in [(0, -1), (-1, 0), (0, 1), (1, 0)] {
            let newR = startRowIdx + r, newC = startColIdx + c
            if newR < 0 || newR >= m || newC < 0 || newC >= n || visitedGrid[newR][newC] != -1 {
                continue
            }
            let cellVal = grid[newR][newC]
            visitedGrid[newR][newC] = 0 // marking this cell as visited
            if cellVal == 0 {
                shortestPathDFSHelper(grid, k, remainingK, newR, newC, currentSteps + 1, &minSteps, &visitedGrid)
            } else {
                shortestPathDFSHelper(grid, k, remainingK - 1, newR, newC, currentSteps + 1, &minSteps, &visitedGrid)
            }
            visitedGrid[newR][newC] = -1 // backtracking
        }
    }
}


// BFS with memoization. Accepted
class Solution {
    func shortestPath(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count, n = grid[0].count
        var minSteps = Int.max, visitedGrid = Array(repeating: Array(repeating: Array(repeating: -1,
                                                                                      count: k + 1),
                                                                     count: n),
                                                    count: m)
        var queue = [(Int, Int, Int, Int)]() // (row, col, currentSteps, remainingRemoval)
        queue.append((0, 0, 0, k))
        while !queue.isEmpty {
            let (row, col, currentSteps, remainingRemoval) = queue.removeFirst()
            visitedGrid[row][col][remainingRemoval] = 0 // marking it as visited
            if row == m - 1 && col == n - 1 && remainingRemoval >= 0 {
                minSteps = min(minSteps, currentSteps)
            }
            
            for (r, c) in [(0, -1), (-1, 0), (0, 1), (1, 0)] {
                let newR = row + r, newC = col + c
                if newR < 0 || newR >= m || newC < 0 || newC >= n  {
                    continue
                }
                
                let cellVal = grid[newR][newC]
                let newRemainingRemoval = cellVal == 0 ? remainingRemoval : remainingRemoval - 1
                if newRemainingRemoval < 0 || visitedGrid[newR][newC][newRemainingRemoval] != -1  {
                    continue
                }
                
                visitedGrid[newR][newC][newRemainingRemoval] = 0 // marking this cell as visited
                queue.append((newR, newC, currentSteps + 1, newRemainingRemoval))
            }
        }
        return minSteps == Int.max ? -1 : minSteps
    }
}
