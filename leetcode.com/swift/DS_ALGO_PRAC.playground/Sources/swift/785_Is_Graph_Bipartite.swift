import Foundation
// BFS
class Solution {
    func isBipartite(_ graph: [[Int]]) -> Bool {
        guard graph.count > 0 else {
            return false
        }
        for i in 0..<graph.count {
            var colorMap = [Int:String]()
            colorMap[i] = "RED"
            var nodeQueue = [(i, "RED")]
            while !nodeQueue.isEmpty {
                var (node, color) = nodeQueue.removeFirst()
                for neighbour in graph[node] {
                    if let neighbourColor = colorMap[neighbour] {
                        if neighbourColor == color {
                            return false
                        }
                    } else {
                        if color == "RED" {
                            nodeQueue.append((neighbour, "BLUE"))
                            colorMap[neighbour] = "BLUE"
                        } else {
                            nodeQueue.append((neighbour, "RED"))
                            colorMap[neighbour] = "RED"
                        }
                    }
                }
            }
        }
        return true
    }
}
