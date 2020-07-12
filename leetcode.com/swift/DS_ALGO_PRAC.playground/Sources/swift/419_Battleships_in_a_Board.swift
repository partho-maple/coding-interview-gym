// Time: O(n) | Space: O(n)
import Foundation
class Solution {
    func countBattleships(_ board: [[Character]]) -> Int {
        var visitedCells = Set<String>()
        var connectedComponentsCount = 0
        for i in 0..<board.count {
            for j in 0..<board[0].count {
                if !visitedCells.contains("\(i)-\(j)") && String(board[i][j]) == "X" {
                    visitedCells.insert("\(i)-\(j)")
                    countBattleshipsDFSHelper(board, i, j, &visitedCells)
                    connectedComponentsCount += 1
                }
            }
        }
        return connectedComponentsCount
    }
    
    private func countBattleshipsDFSHelper(_ board: [[Character]], _ i: Int, _ j: Int, _ visitedCells: inout Set<String>) {
        for neighbour in [(-1,0),(0,1),(1,0),(0,-1)] {
            let (newRow, newCol) = (i + neighbour.0, j + neighbour.1)
            if newRow >= 0 && newRow < board.count && newCol >= 0 && newCol < board[0].count && !visitedCells.contains("\(newRow)-\(newCol)") && String(board[i][j]) == "X"  {
                visitedCells.insert("\(newRow)-\(newCol)")
                countBattleshipsDFSHelper(board, newRow, newCol, &visitedCells)
            }
        }
    }
}
