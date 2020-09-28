// DFS
import Foundation
class Solution {
    func wallsAndGates(_ rooms: inout [[Int]]) {
        
        var visited = Set<String>()
        for i in 0..<rooms.count {
            for j in 0..<rooms[0].count {
                if rooms[i][j] == 0 {
                    wallsAndGatesDFSHelper(&rooms, &visited, (i, j))
                }
            }
        }
    }
    
    func wallsAndGatesDFSHelper(_ rooms: inout [[Int]], _ visited: inout Set<String>, _ startCoord: (Int, Int)) {
        for neighbor in [ (-1,0), (0,1), (1,0), (0,-1) ] {
            let (newX, newY) = (startCoord.0 + neighbor.0, startCoord.1 + neighbor.1)
            if newX >= 0 && newX < rooms.count && newY >= 0 && newY < rooms[0].count && rooms[newX][newY] != -1 && rooms[newX][newY] != 0 && !visited.contains("\(newX)-\(newY)") {
                if rooms[newX][newY] > rooms[startCoord.0][startCoord.1] {
                    rooms[newX][newY] = rooms[startCoord.0][startCoord.1] + 1
                    visited.insert("\(newX)-\(newY)")
                    wallsAndGatesDFSHelper(&rooms, &visited, (newX, newY))
                    visited.remove("\(newX)-\(newY)")
                }
            }
        }
    }
}

// BFS
import Foundation
class Solution {
    func wallsAndGates(_ rooms: inout [[Int]]) {
        
        var queue = [(Int, Int, Int)]()
        var visited = Set<String>()
        for i in 0..<rooms.count {
            for j in 0..<rooms[0].count {
                if rooms[i][j] == 0 {
                    queue.append((i, j, 0))
                }
            }
        }
        
        while !queue.isEmpty {
            var currentLevelLength = queue.count
            for _ in 1...currentLevelLength {
                let (x, y, val) = queue.removeFirst()
                
                for neighbor in [ (-1,0), (0,1), (1,0), (0,-1) ] {
                    let (newX, newY) = (x + neighbor.0, y + neighbor.1)
                    if newX >= 0 && newX < rooms.count && newY >= 0 && newY < rooms[0].count && rooms[newX][newY] != -1 && rooms[newX][newY] != 0 && !visited.contains("\(newX)-\(newY)") {
                        rooms[newX][newY] = val + 1
                        visited.insert("\(newX)-\(newY)")
                        queue.append((newX, newY, val + 1))
                    }
                }
            }
        }
    }
}
