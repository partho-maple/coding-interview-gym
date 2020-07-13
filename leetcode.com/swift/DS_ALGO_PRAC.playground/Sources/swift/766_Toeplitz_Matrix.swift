import Foundation

// Time: O(MN) |  Accepted
// Vaive brute force. Code became overwhelming, need to simplify it and also need to address the followups
// My first solution
class Solution {
    func isToeplitzMatrix(_ matrix: [[Int]]) -> Bool {
        let (rowCount, colCount) = (matrix.count, matrix[0].count)
        var (currentRow, currentCol, currentDiagonal) = (rowCount - 1, 0, 1)
        while currentDiagonal < (rowCount + colCount) {
            currentDiagonal += 1
            
            // Checking the values on same diagon
            let currVal = matrix[currentRow][currentCol]
            var (nextRow, nextCol) = (currentRow + 1, currentCol + 1)
            while nextRow < rowCount && nextCol < colCount {
                let nextVal = matrix[nextRow][nextCol]
                if currVal == nextVal {
                    nextRow += 1
                    nextCol += 1
                } else {
                    return false
                }
            }
            
            // changing/moving to next diagon
            if currentRow > 0 {
                currentRow -= 1
                currentCol = 0
            } else {
                currentRow = 0
                currentCol += 1
            }
            
        }
        return true
    }
}


// https://tinyurl.com/ydz3k3wn
// Approach #1: Group by Category [Accepted]
class Solution {
    func isToeplitzMatrix(_ matrix: [[Int]]) -> Bool {
        let (rowCount, colCount) = (matrix.count, matrix[0].count)
        var diagonalValurMap = [Int: Int]()
        for i in 0..<rowCount {
            for j in 0..<colCount {
                let diagonalIdx = i - j
                if let diagonalVal = diagonalValurMap[diagonalIdx] {
                    if diagonalVal != matrix[i][j] {
                        return false
                    }
                } else {
                    diagonalValurMap[diagonalIdx] = matrix[i][j]
                }
            }
        }
        return true
    }
}


// https://tinyurl.com/ydz3k3wn
// Approach #2: Compare With Top-Left Neighbor [Accepted]
class Solution {
    func isToeplitzMatrix(_ matrix: [[Int]]) -> Bool {
        let (rowCount, colCount) = (matrix.count, matrix[0].count)
        for i in 0..<rowCount {
            for j in 0..<colCount {
                if i - 1 >= 0 && j - 1 >= 0 && matrix[i - 1][j - 1] != matrix[i][j] {
                    return false
                }
            }
        }
        return true
    }
}
