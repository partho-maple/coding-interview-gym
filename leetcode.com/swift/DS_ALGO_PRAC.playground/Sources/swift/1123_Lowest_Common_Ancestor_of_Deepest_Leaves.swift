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
import Foundation
class Solution {
    func lcaDeepestLeaves(_ root: TreeNode?) -> TreeNode? {
        var levelNodeMap = [Int:[Int]]()
        guard let node = root else {
            return root
        }
        
        var nodeQueue = [TreeNode]()
        nodeQueue.append(node)
        var currentDepth = -1
        
        // Doing BFS to get the deepest node
        while nodeQueue.count > 0 {
            currentDepth += 1
            levelNodeMap[currentDepth] = [Int]()
            var currentLevelLength = nodeQueue.count
            while currentLevelLength > 0 {
                let currentNode = nodeQueue.removeFirst()
                currentLevelLength -= 1
                levelNodeMap[currentDepth]!.append(currentNode.val)
                if let left = currentNode.left {
                    nodeQueue.append(left)
                }
                if let right = currentNode.right {
                    nodeQueue.append(right)
                }
            }
        }
        
        // Doing DFS to get the LCA of deepest nodes
        if let lca = lcaDeepestLeavesDFSHelper(node, Set<Int>(levelNodeMap[currentDepth]!)) {
            return lca
        } else {
            return nil
        }
    }
    
    func lcaDeepestLeavesDFSHelper(_ root: TreeNode?, _ deepestNodes: Set<Int>) -> TreeNode? {
        guard let root = root else {
            return nil
        }
        if deepestNodes.contains(root.val) {
            return root
        }
        let left = lcaDeepestLeavesDFSHelper(root.left, deepestNodes)
        let right = lcaDeepestLeavesDFSHelper(root.right, deepestNodes)
        
        if let left = left, let right = right {
            return root
        }
        if let left = left {
            return left
        }
        if let right = right {
            return right
        }
        return nil
    }
}
