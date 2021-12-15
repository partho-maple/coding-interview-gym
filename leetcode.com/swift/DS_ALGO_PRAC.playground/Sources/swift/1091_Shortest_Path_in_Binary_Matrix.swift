class Solution {
    func shortestPathBinaryMatrix(_ grid: [[Int]]) -> Int {
        var copyGrid = grid, n = grid.count, queue = [(Int, Int, Int)](), minLength = Int.max
        queue.append((0, 0 ,1))
        while !queue.isEmpty {
            let (row, col, length) = queue.removeFirst()
            if row == n - 1 && col == n - 1 {
                minLength = length
                queue.removeAll()
                break
            }
            for (r, c) in [(0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)] {
                let (newR, newC) = (row + r, col + c)
                if newR < 0 || newR >= copyGrid.count || newC < 0 || newC >= copyGrid[0].count || copyGrid[newR][newC] != 0 {
                    continue
                }
                copyGrid[newR][newC] = 2
                queue.append((newR, newC, length + 1))
            }
        }
        return minLength
    }
}
