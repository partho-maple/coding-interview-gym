// Main Idea: https://tinyurl.com/y4dtahmr
class Solution {
    func containsCycle(_ grid: [[Character]]) -> Bool {
        var visited = Array(repeating: Array(repeating: false, count: grid[0].count), count: grid.count)
        for i in 0..<grid.count {
            for j in 0..<grid[0].count {
                if !visited[i][j] {
                    if containsCycleHelperDFS(grid, i, j, &visited, -1, -1) {
                        return true
                    }
                }
            }
        }
        return false
    }
    
    func containsCycleHelperDFS(_ grid: [[Character]], _ row: Int, _ col: Int, _ visited: inout [[Bool]], _ prevRow: Int, _ prevCol: Int) -> Bool {
        for (r, c) in [(0, -1), (-1, 0), (0, 1), (1, 0)] {
            let (newR, newC) = (row + r, col + c)
            if newR < 0 || newR >= grid.count || newC < 0 || newC >= grid[0].count {
                continue
            }
            if newR == prevRow && newC == prevCol {
                continue
            }
            if grid[newR][newC] == grid[row][col] {
                if visited[newR][newC] {
                    return true
                } else {
                    visited[newR][newC] = true
                    if containsCycleHelperDFS(grid, newR, newC, &visited, row, col) {
                        return true
                    }
                }
            }
        }
        return false
    }
}
