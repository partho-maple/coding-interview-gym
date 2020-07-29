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
    func rightSideView(_ root: TreeNode?) -> [Int] {
        guard var root = root else {
            return []
        }
        var rightView = [Int]()
        var (maxDepthSoFar, currentDepth) = (-1, -1)
        rightSideViewDFSHelper(root, currentDepth + 1, &maxDepthSoFar, &rightView)
        return rightView
    }
    
    private func rightSideViewDFSHelper(_ root: TreeNode?, _ currentDepth: Int, _ maxDepthSoFar: inout Int, _ rightView: inout [Int]) {
        guard var root = root else {
            return
        }
        if currentDepth > maxDepthSoFar {
            rightView.append(root.val)
            maxDepthSoFar = currentDepth
        }
        rightSideViewDFSHelper(root.right, currentDepth + 1, &maxDepthSoFar, &rightView)
        rightSideViewDFSHelper(root.left, currentDepth + 1, &maxDepthSoFar, &rightView)
    }
}
