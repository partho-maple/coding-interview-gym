import Foundation

class Solution {
    func gameOfLife(_ board: inout [[Int]]) {
        guard board.count > 0 else {
            return
        }
        guard board[0].count > 0 else {
            return
        }
        let rows = board.count
        let cols = board[0].count
        for row in 0..<rows {
            for col in 0..<cols {
                let livingNeighbours = self.getLivesCount(row, col, board)
                if (board[row][col] == 1) && (livingNeighbours < 2 || livingNeighbours > 3) {
                    board[row][col] = -1
                }
                if board[row][col] == 0 && livingNeighbours == 3 {
                    board[row][col] = 2
                }
            }
        }
        for row in 0..<rows {
            for col in 0..<cols {
                if board[row][col] > 0 {
                    board[row][col] = 1
                } else {
                    board[row][col] = 0
                }
            }
        }
    }
    
    private func getLivesCount(_ row: Int, _  col: Int, _ board: [[Int]]) -> Int {
        let rows = board.count
        let cols = board[0].count
        var neighbours = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        var livingNeighbours = 0
        for neighbour in neighbours {
            let r = row + neighbour.0
            let c = col + neighbour.1
            if (r < rows && r >= 0) && (c < cols && c >= 0) && (abs(board[r][c]) == 1) {
                livingNeighbours += 1
            }
         }
        return livingNeighbours
    }
}


