import Foundation
class Solution {
    func shortestBridge(_ A: [[Int]]) -> Int {
        var firstIland = [(Int, Int)]()
        var grids = A
        var found = false
        for i in 0..<grids.count {
            for j in 0..<grids[0].count {
                if grids[i][j] == 1 {
                    firstIland.append((i,j))
                    grids[i][j] = 99
                    getIlandsDFSHelper(&grids, i, j, &firstIland)
                    found = true
                    break
                }
            }
            if found == true {
                break
            }
        }
        
        var currentLevel = -1
        while firstIland.count > 0 {
            currentLevel += 1
            var currentLevelLength = firstIland.count
            while currentLevelLength > 0 {
                currentLevelLength -= 1
                let (i, j) = firstIland.removeFirst()
                for neighbour in [(-1,0),(0,1),(1,0),(0,-1)] {
                    let (newI, newJ) = (i + neighbour.0, j + neighbour.1)
                    if newI >= 0 && newI < grids.count && newJ >= 0 && newJ < grids[i].count && grids[newI][newJ] != 99 {
                        if grids[newI][newJ] == 1 {
                            return currentLevel
                        }
                        grids[newI][newJ] = 99
                        firstIland.append((newI, newJ))
                    }
                }
            }
        }
        return currentLevel
    }
    
    private func getIlandsDFSHelper(_ grids: inout [[Int]], _ i: Int, _ j: Int, _ firstIland: inout [(Int, Int)]) {
        for neighbour in [(-1,0),(0,1),(1,0),(0,-1)] {
            let (newI, newJ) = (i + neighbour.0, j + neighbour.1)
            if newI >= 0 && newI < grids.count && newJ >= 0 && newJ < grids[i].count && grids[newI][newJ] == 1 {
                grids[newI][newJ] = 99
                firstIland.append((newI, newJ))
                getIlandsDFSHelper(&grids, newI, newJ, &firstIland)
            }
        }
    }
}
