import Foundation

class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        guard matrix.count > 0 else {
            return []
        }
        var rowCount = matrix.count
        var colCount = matrix[0].count
        print("rowCount: \(rowCount), colCount: \(colCount)")
        var seen = Array(repeating: Array(repeating: false, count: colCount), count: rowCount)
        print("seen: \(seen)")
        var ans = [Int]()
        var rowDirection = [0, 1, 0, -1]
        var colDirection = [1, 0, -1, 0]
        var row = 0, col = 0, directionIdx = 0
        for _ in 0..<(rowCount*colCount) {
            print("-------------------------")
            print("row: \(row), col: \(col), directionIdx: \(directionIdx)")
            ans.append(matrix[row][col])
            seen[row][col] = true
            var cRow = row + rowDirection[directionIdx]
            var cCol = col + colDirection[directionIdx]
            print("cRow: \(cRow), cCol: \(cCol)")
            if (0 <= cRow) && (cRow < rowCount) && (0 <= cCol ) && (cCol < colCount) && (seen[cRow][cCol] == false) {
                row = cRow
                col = cCol
            } else {
                directionIdx = (directionIdx + 1) % 4
                row = row + rowDirection[directionIdx]
                col = col + colDirection[directionIdx]
            }
        }
        return ans
    }
}
