import Foundation

// My initial solution during contest. Time limit exceeded. 17 / 26 test cases passed. But all test cases are passing is i run individually.
class Solution {
    func treeDiameter(_ edges: [[Int]]) -> Int {
        var graph = [Int:[Int]]()
        for edge in edges {
            let (u, v) = (edge[0], edge[1])
            graph[u, default: [Int]()].append(v)
            graph[v, default: [Int]()].append(u)
        }
        var visited = Set<Int>()
        var diameters = [Int]()
        for node in graph.keys {
            if !visited.contains(node) {
                let (longestDepth, diameter) = nodeDiameterAndPathFrom(rootNode: node, originalGraph: graph, visitedSet: &visited)
                visited.removeAll()
                diameters.append(diameter)
            }
        }
        return diameters.max() ?? 0
    }
    
    private func nodeDiameterAndPathFrom(rootNode node: Int?, originalGraph graph: [Int:[Int]], visitedSet visited: inout Set<Int>) -> (Int, Int) {
        guard let node = node else {
            return (0, 0)
        }
        visited.insert(node)
        var (longestDepth, diameter) = (0, 0)
        var childrensInfo = [(Int, Int)]()
        for child in graph[node]! {
            if !visited.contains(child) {
                childrensInfo.append(nodeDiameterAndPathFrom(rootNode: child, originalGraph: graph, visitedSet: &visited))
            }
        }
        var depths = childrensInfo.map { $0.0 }.sorted(by: >)
        if depths.count > 1 {
            longestDepth = depths[0] + 1
            diameter =  depths[0] +  depths[1] + 2
        } else if depths.count == 1 {
            longestDepth = depths[0] + 1
            diameter =  max(longestDepth, childrensInfo[0].1)
        }
        return (longestDepth, diameter)
    }
}






// DFS, Top-Down
import Foundation
class Solution {
    func treeDiameter(_ edges: [[Int]]) -> Int {
        var graph = [Int:[Int]]()
        for edge in edges {
            let (u, v) = (edge[0], edge[1])
            graph[u, default: [Int]()].append(v)
            graph[v, default: [Int]()].append(u)
        }
        var visited = Set<Int>()
        var maxDiameter = 0
        for node in graph.keys {
            if !visited.contains(node) {
                treeDiameterDFSHelper(rootNode: node, originalGraph: graph, visitedSet: &visited, currentMaxDiameter: &maxDiameter)
            }
        }
        return maxDiameter
    }
    
    private func treeDiameterDFSHelper(rootNode node: Int?, originalGraph graph: [Int:[Int]], visitedSet visited: inout Set<Int>, currentMaxDiameter maxDiameter: inout Int) -> Int {
        guard let node = node else {
            return 0
        }
        visited.insert(node)
        var childrensDepths = [Int]()
        for child in graph[node]! {
            if !visited.contains(child) {
                childrensDepths.append(treeDiameterDFSHelper(rootNode: child, originalGraph: graph, visitedSet: &visited, currentMaxDiameter: &maxDiameter))
            }
        }
        childrensDepths.sort(by: >)
        if childrensDepths.count <= 0 {
            return 1
        } else if childrensDepths.count == 1 {
            maxDiameter = max(maxDiameter, childrensDepths.first!)
            return 1 + childrensDepths.first!
        } else {
            maxDiameter = max(maxDiameter, childrensDepths[..<2].reduce(0, +))
            return 1 + childrensDepths.first!
        }
    }
}




// 2 BFS
// Explanation: https://www.geeksforgeeks.org/longest-path-undirected-tree/
import Foundation
class Solution {
    func treeDiameter(_ edges: [[Int]]) -> Int {
        guard edges.count > 0 else {
            return 0
        }
        var graph = [Int:[Int]]()
        for edge in edges {
            let (u, v) = (edge[0], edge[1])
            graph[u, default: [Int]()].append(v)
            graph[v, default: [Int]()].append(u)
        }
        let (farthestNode, _) = treeDiameterBFSHelper(rootNode: graph.keys.first!, originalGraph: graph)
        let (_, diameter) = treeDiameterBFSHelper(rootNode: farthestNode, originalGraph: graph)
        return diameter
    }
    
    private func treeDiameterBFSHelper(rootNode root: Int, originalGraph graph: [Int:[Int]]) -> (Int, Int) {
        var diameter = -1 // diameter is the count of edges
        var lastNode = root
        var visited = Set<Int>()
        visited.insert(root)
        var nodeQueue = Array([root])
        print(nodeQueue)
        while nodeQueue.count > 0 {
            var currentLevelLength = nodeQueue.count
            diameter += 1
            for _ in 0..<currentLevelLength {
                let node = nodeQueue.removeFirst()
                for child in graph[node]! {
                    if !visited.contains(child) {
                        visited.insert(child)
                        nodeQueue.append(child)
                        lastNode = child
                    }
                }
            }
        }
        return (lastNode, diameter)
        
    }
}
