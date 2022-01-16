import Foundation


/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var neighbors: [Node?]
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.neighbors = []
 *     }
 * }
 */

class Solution {
    func cloneGraph(_ node: Node?) -> Node? {
        guard let node = node else { return node}
        var visited = [Int: Node]()
        return cloneGraphHelper(node, &visited)
    }
    
    func cloneGraphHelper(_ node: Node, _ visited: inout [Int: Node]) -> Node {
        if let existingNode = visited[node.val] {
            return existingNode
        }
        
        visited[node.val] = Node(node.val)
        node.neighbors.forEach { neighbor in
            if let unWrappedNeighbor = neighbor {
                visited[node.val]?.neighbors.append(self.cloneGraphHelper(unWrappedNeighbor, &visited))
            }
        }
        return visited[node.val]!
    }
}

