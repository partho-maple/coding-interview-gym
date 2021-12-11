class Solution {
    func largestIsland(_ grid: [[Int]]) -> Int {
        var connectedGrid = grid
        var parentID = 2, parentLengthMap = [Int:Int]()
        for row in 0..<grid.count {
            for col in 0..<grid[0].count {
                if connectedGrid[row][col] == 1 {
                    var currentLength = 1
                    largestIslandDFSHelper(row, col, &connectedGrid, parentID, &currentLength)
                    parentLengthMap[parentID] = currentLength
                    parentID += 1
                }
            }
        }
        
        var maxLength = Int.min
        for row in 0..<grid.count {
            for col in 0..<grid[0].count {
                if connectedGrid[row][col] == 0 {
                    var currentLength = 1, parentIdSet = Set<Int>()
                    for (r, c) in [(0, -1), (-1, 0), (0, 1), (1, 0)] {
                        let (newR, newC) = (row + r, col + c)
                        if newR < 0 || newR >= connectedGrid.count || newC < 0 || newC >= connectedGrid[0].count || connectedGrid[newR][newC] == 0 {
                            continue
                        }
                        let currentParentID = connectedGrid[newR][newC]
                        if !parentIdSet.contains(currentParentID) {
                            currentLength += parentLengthMap[currentParentID]!
                            parentIdSet.insert(currentParentID)
                        }
                    }
                    maxLength = max(maxLength, currentLength)
                }
            }
        }
        return maxLength == Int.min ? parentLengthMap.values.first! : maxLength
    }
    
    func largestIslandDFSHelper(_ row: Int, _ col: Int, _ connectedGrid: inout [[Int]], _ parentID: Int, _ currentLength: inout Int) {
        connectedGrid[row][col] = parentID
        for (r, c) in [(0, -1), (-1, 0), (0, 1), (1, 0)] {
            let (newR, newC) = (row + r, col + c)
            if newR < 0 || newR >= connectedGrid.count || newC < 0 || newC >= connectedGrid[0].count || connectedGrid[newR][newC] != 1 {
                continue
            }
            currentLength += 1
            largestIslandDFSHelper(newR, newC, &connectedGrid, parentID, &currentLength)
        }
    }
}
