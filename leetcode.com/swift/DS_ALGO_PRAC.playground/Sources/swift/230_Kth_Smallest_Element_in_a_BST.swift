import Foundation

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */

// Brute force solution. Time and Space both O(n). It perfofms an exustive search through the whole BST
class Solution {
    func kthSmallest(_ root: TreeNode?, _ k: Int) -> Int {
        return inorderTraversal(root)[k - 1]
    }
    
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        guard let node = root else { return []}
        let leftNodes = inorderTraversal(node.left)
        let rightNode = inorderTraversal(node.right)
        return leftNodes + [node.val] + rightNode
    }
}

