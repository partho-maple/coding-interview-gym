import Foundation

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */

// DFS. Wrong answer
class Solution {
    func verticalOrder(_ root: TreeNode?) -> [[Int]] {
        var heightNodeMap = [Int:[Int]]()
        verticalOrderDFSHelper(root, 0, &heightNodeMap)
        
        var result = [[Int]]()
        for key in heightNodeMap.keys.sorted() {
            result.append(heightNodeMap[key]!.sorted())
        }
        return result
    }
    
    func verticalOrderDFSHelper(_ root: TreeNode?, _ horrizotalDistace: Int, _ heightNodeMap: inout [Int:[Int]]) {
        guard let root = root else {
            return
        }
        
        heightNodeMap[horrizotalDistace, default: [Int]()].append(root.val)
        verticalOrderDFSHelper(root.left, horrizotalDistace - 1, &heightNodeMap)
        verticalOrderDFSHelper(root.right, horrizotalDistace + 1, &heightNodeMap)
    }
}

// BFS. Accepted
class Solution {
    func verticalOrder(_ root: TreeNode?) -> [[Int]] {
        guard let root = root else {
            return []
        }
        var heightNodeMap = [Int:[Int]]()
        var queue = [(TreeNode, Int)]() // (TreeNode, horrizotalDistace)
        queue.append((root, 0))
        
        while !queue.isEmpty {
            let (node, horrizotalDistace) = queue.removeFirst()
            heightNodeMap[horrizotalDistace, default: [Int]()].append(node.val)
            if let left = node.left {
                queue.append((left, horrizotalDistace - 1))
            }
            
            if let right = node.right {
                queue.append((right, horrizotalDistace + 1))
            }
        }
        
        var result = [[Int]](), minHorrizotalDistace = heightNodeMap.keys.min()!, maxHorrizotalDistace = heightNodeMap.keys.max()!
        for key in minHorrizotalDistace...maxHorrizotalDistace {
            result.append(heightNodeMap[key]!)
        }
        return result
    }
}
