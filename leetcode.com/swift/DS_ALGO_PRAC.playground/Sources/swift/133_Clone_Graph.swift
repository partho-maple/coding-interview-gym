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
        guard let unWrappedNode = node else { return node}
        
        var nodeDict = [Int: Node]()
        let clonedNode = self.cloneGraphHelper(unWrappedNode, &nodeDict)
        return clonedNode
    }
    
    func cloneGraphHelper(_ node: Node, _ nodeDict: inout [Int: Node]) -> Node {
        if let existingNode = nodeDict[node.val] {
            return existingNode
        }
        
        var clonedNode = Node(node.val)
        nodeDict[node.val] = clonedNode
        node.neighbors.forEach {neighbor in
            if let unWrappedNeighbor = neighbor {
                let clonedNeighbour = self.cloneGraphHelper(unWrappedNeighbor, &nodeDict)
                nodeDict[node.val]?.neighbors.append(clonedNeighbour)
            }
        }
        return clonedNode
    }
}

