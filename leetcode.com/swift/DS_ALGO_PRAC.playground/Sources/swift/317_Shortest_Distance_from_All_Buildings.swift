import Foundation

// Brute force. Time: O(n^2 * m^2). Got TLE. 53 / 72 test cases passed.
class Solution {
    func shortestDistance(_ grid: [[Int]]) -> Int {
        var allBuildingsSet = Set<String>()
        var (rowCount, colCount) = (grid.count, grid[0].count)
        for i in 0..<rowCount {
            for j in 0..<colCount {
                if grid[i][j] == 1 {
                    allBuildingsSet.insert("\(i)-\(j)")
                }
            }
        }
        
        var minDistance = Int.max
        for i in 0..<rowCount {
            for j in 0..<colCount {
                if grid[i][j] == 0 {
                    var currentTotalDistance = shortestDistanceBFSHelper(grid, allBuildingsSet, i, j)
                    minDistance = min(minDistance, currentTotalDistance)
                }
            }
        }
        return minDistance != Int.max ? minDistance : -1
    }
    
    private func shortestDistanceBFSHelper(_ grid: [[Int]], _ allBuildingsSet: Set<String>, _ startRowIdx: Int, _ startColIdx: Int) -> Int {
        var queue = Array([(startRowIdx, startColIdx)])
        var (currentDistance, currentTotalDistance) = (0, 0)
        var currentBuildings = Set<String>()
        var visited = Set<String>()
        visited.insert("\(startRowIdx)-\(startColIdx)")
        while queue.count > 0 {
            currentDistance += 1
            var currentLevelLength = queue.count
            while currentLevelLength > 0 {
                currentLevelLength -= 1
                let (row, col) = queue.removeFirst()
                for neighbour in [(-1,0),(0,1),(1,0),(0,-1)] {
                    let (newRowIdx, newColIdx) = (row + neighbour.0, col + neighbour.1)
                    if newRowIdx >= 0 && newRowIdx < grid.count && newColIdx >= 0 && newColIdx < grid[0].count && !visited.contains("\(newRowIdx)-\(newColIdx)") {
                        visited.insert("\(newRowIdx)-\(newColIdx)")
                        if grid[newRowIdx][newColIdx] == 0 {
                            queue.append((newRowIdx, newColIdx))
                        } else if grid[newRowIdx][newColIdx] == 1 {
                            currentBuildings.insert("\(newRowIdx)-\(newColIdx)")
                            currentTotalDistance += currentDistance
                        } else if grid[newRowIdx][newColIdx] == 2 {
                            // Can't pass, so do nothing
                        }
                    }
                }
            }
        }
        return allBuildingsSet.count == currentBuildings.count ? currentTotalDistance : Int.max
    }
}


// Brute force. Time: O(n^2 * m^2). Got Accepted. Early pruning optimisation
class Solution {
    func shortestDistance(_ grid: [[Int]]) -> Int {
        var allBuildingsSet = Set<String>()
        var (rowCount, colCount) = (grid.count, grid[0].count)
        for i in 0..<rowCount {
            for j in 0..<colCount {
                if grid[i][j] == 1 {
                    allBuildingsSet.insert("\(i)-\(j)")
                }
            }
        }
        
        var minDistance = Int.max
        for i in 0..<rowCount {
            for j in 0..<colCount {
                if grid[i][j] == 0 {
                    var (currentTotalDistance, buildingReached) = shortestDistanceBFSHelper(grid, allBuildingsSet, i, j)
                    minDistance = min(minDistance, currentTotalDistance)
                } else if grid[i][j] == 1 {
                    var (currentTotalDistance, buildingReached) = shortestDistanceBFSHelper(grid, allBuildingsSet, i, j)
                    if buildingReached != (allBuildingsSet.count - 1) {
                        return -1
                    }
                }
            }
        }
        return minDistance != Int.max ? minDistance : -1
    }
    
    private func shortestDistanceBFSHelper(_ grid: [[Int]], _ allBuildingsSet: Set<String>, _ startRowIdx: Int, _ startColIdx: Int) -> (Int, Int) {
        var queue = Array([(startRowIdx, startColIdx)])
        var (currentDistance, currentTotalDistance) = (0, 0)
        var currentBuildings = Set<String>()
        var visited = Set<String>()
        visited.insert("\(startRowIdx)-\(startColIdx)")
        while queue.count > 0 {
            currentDistance += 1
            var currentLevelLength = queue.count
            while currentLevelLength > 0 {
                currentLevelLength -= 1
                let (row, col) = queue.removeFirst()
                for neighbour in [(-1,0),(0,1),(1,0),(0,-1)] {
                    let (newRowIdx, newColIdx) = (row + neighbour.0, col + neighbour.1)
                    if newRowIdx >= 0 && newRowIdx < grid.count && newColIdx >= 0 && newColIdx < grid[0].count && !visited.contains("\(newRowIdx)-\(newColIdx)") {
                        visited.insert("\(newRowIdx)-\(newColIdx)")
                        if grid[newRowIdx][newColIdx] == 0 {
                            queue.append((newRowIdx, newColIdx))
                        } else if grid[newRowIdx][newColIdx] == 1 {
                            currentBuildings.insert("\(newRowIdx)-\(newColIdx)")
                            currentTotalDistance += currentDistance
                        } else if grid[newRowIdx][newColIdx] == 2 {
                        }
                    }
                }
            }
        }
        return (allBuildingsSet.count == currentBuildings.count ? currentTotalDistance : Int.max, currentBuildings.count)
    }
}
