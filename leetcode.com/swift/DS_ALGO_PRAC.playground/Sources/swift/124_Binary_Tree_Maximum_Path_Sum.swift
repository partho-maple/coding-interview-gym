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
class Solution {
    func maxPathSum(_ root: TreeNode?) -> Int {
        var maxSumResult: Int = Int.min
        maxPathSumDFSHelper(root, &maxSumResult)
        return maxSumResult
    }
    
    private func maxPathSumDFSHelper(_ root: TreeNode?, _ maxSumResult: inout Int) -> Int {
        guard let root = root else {
            return 0
        }
        let leftMaxSum = maxPathSumDFSHelper(root.left, &maxSumResult)
        let rightMaxSum = maxPathSumDFSHelper(root.right, &maxSumResult)
        
        maxSumResult = [maxSumResult, root.val, root.val + leftMaxSum, root.val + rightMaxSum, root.val + leftMaxSum + rightMaxSum].max()!
        
        return [root.val, root.val + leftMaxSum, root.val + rightMaxSum].max()!
    }
}
