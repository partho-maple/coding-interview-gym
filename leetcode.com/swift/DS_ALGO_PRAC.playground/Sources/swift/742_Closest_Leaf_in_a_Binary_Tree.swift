import Foundation

class Solution {
    func findClosestLeaf(_ root: TreeNode?, _ k: Int) -> Int {
        var graph = [Int:[Int]](), queue = [(TreeNode?, TreeNode)]() // (currentNode, parentNode)
        queue.append((root, TreeNode(Int.max)))

        // Creates the graph.
        while !queue.isEmpty {
            let (node, parentNode) = queue.removeFirst()
            if let node = node {
                graph[node.val, default: [Int]()].append(parentNode.val)
                graph[parentNode.val, default: [Int]()].append(node.val)
                queue.append((node.left, node))
                queue.append((node.right, node))
            }
        }

        var valQueue = [Int](), visited = Set<Int>()
        valQueue.append(k)
        while !valQueue.isEmpty {
            let currentNodeVal = valQueue.removeFirst()
            visited.insert(currentNodeVal)
            if let neighbours = graph[currentNodeVal] {
                if neighbours.count <= 1 && currentNodeVal != Int.max {
                    return currentNodeVal
                }
                for i in 0..<neighbours.count {
                    let neighbour = neighbours[i]
                    if !visited.contains(neighbour) {
                        valQueue.append(neighbour)
                    }
                }
            } else {
                return currentNodeVal
            }
        }
        return -1
    }
}
