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
    func findDuplicateSubtrees(_ root: TreeNode?) -> [TreeNode?] {
        guard let root = root else {
            return []
        }
        
        var counter = [[String]:Int]()
        var duplicates = [TreeNode]()
        
        nodeCountDFS(root, &counter, &duplicates)

        return duplicates
    }
    
    func nodeCountDFS(_ root: TreeNode?, _ counter: inout [[String]:Int], _ duplicates: inout [TreeNode]) -> [String] {
        guard let root = root else {
            return ["#"]
        }

        var inorder = [String]()
        let left = nodeCountDFS(root.left, &counter, &duplicates)
        let right = nodeCountDFS(root.right, &counter, &duplicates)
        inorder = left + [String(root.val)] + right
        counter[inorder, default: 0] += 1
        
        if counter[inorder] == 2 {
            duplicates.append(root)
        }
        
        return inorder
    }
}
