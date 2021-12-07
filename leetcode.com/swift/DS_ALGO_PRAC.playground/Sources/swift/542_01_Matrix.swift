// Naive BFS, on every cell with "1" value. O(n^2 m^2). TLE
class Solution {
    func updateMatrix(_ mat: [[Int]]) -> [[Int]] {
        var distance = Array(repeating: Array(repeating: Int.max, count: mat[0].count), count: mat.count)
        for row in 0..<mat.count {
            for col in 0..<mat[0].count {
                var queue = [(Int, Int, Int)]() // (row, col, distance)
                if mat[row][col] == 0 {
                    distance[row][col] = 0
                } else {
                    queue.append((row, col, 1))
                }

                while !queue.isEmpty {
                    let (currentRow, currentCol, currentDistance) = queue.removeFirst()
                    for (r, c) in [(-1, 0), (0, 1), (1, 0), (0, -1)] {
                        let (newRow, newCol) = (r + currentRow, c + currentCol)
                        if newRow >= 0 && newRow < mat.count && newCol >= 0 && newCol < mat[0].count {
                            if mat[newRow][newCol] == 0 {
                                distance[row][col] = currentDistance
                                queue.removeAll()
                                break
                            } else {
                                queue.append((newRow, newCol, currentDistance + 1))
                            }
                        }
                    }
                }
            }
        }
        return distance
    }
}

// Improved BFS. O(n m). Accepted. Main idea from here: https://tinyurl.com/yxsgnmxy
class Solution {
    func updateMatrix(_ mat: [[Int]]) -> [[Int]] {
        var distance = Array(repeating: Array(repeating: Int.max, count: mat[0].count), count: mat.count)
        var queue = [(Int, Int)]() // (row, col)
        for row in 0..<mat.count {
            for col in 0..<mat[0].count {
                if mat[row][col] == 0 {
                    queue.append((row, col))
                    distance[row][col] = 0
                }
            }
        }

        while !queue.isEmpty {
            let (currentRow, currentCol) = queue.removeFirst()
            for (r, c) in [(-1, 0), (0, 1), (1, 0), (0, -1)] {
                let (newRow, newCol) = (r + currentRow, c + currentCol)
                if newRow >= 0 && newRow < mat.count && newCol >= 0 && newCol < mat[0].count {
                    if distance[newRow][newCol] == Int.max {  // this cell has not been visited yet
                        distance[newRow][newCol] = distance[currentRow][currentCol] + 1
                        queue.append((newRow, newCol))
                    }
                }
            }
        }

        return distance
    }
}

// DP. O(n m). Accepted. Main idea from here: https://tinyurl.com/yxsgnmxy
class Solution {
    func updateMatrix(_ mat: [[Int]]) -> [[Int]] {
        var distanceDP = Array(repeating: Array(repeating: Int.max, count: mat[0].count), count: mat.count)
        
        // from top to bottom, let to right
        for row in 0..<mat.count {
            for col in 0..<mat[0].count {
                if mat[row][col] == 0 {
                    distanceDP[row][col] = 0
                } else {
                    var left = 0, top = 0
                    if col > 0 {
                        left = distanceDP[row][col - 1]
                    }
                    if row > 0 {
                        top = distanceDP[row - 1][col]
                    }
                    distanceDP[row][col] = min(distanceDP[row][col], min(left, top) + 1)
                }
            }
        }
        
        // from bottom to top, right to left
        for row in stride(from: mat.count - 1, through: 0, by: -1) {
            for col in stride(from: mat[0].count - 1, through: 0, by: -1) {
                if mat[row][col] == 0 {
                    distanceDP[row][col] = 0
                } else {
                    var right = Int.max - 1, bottom = Int.max - 1
                    if col < mat[0].count - 1 {
                        right = distanceDP[row][col + 1]
                    }
                    if row < mat.count - 1 {
                        bottom = distanceDP[row + 1][col]
                    }
                    distanceDP[row][col] = min(distanceDP[row][col], min(right, bottom) + 1)
                }
            }
        }
        
        return distanceDP
    }
}
