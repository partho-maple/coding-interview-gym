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

// Getting wrong answer onn [1,2,3] test case, not sure why?
import Foundation
class Solution {
    func countNodes(_ root: TreeNode?) -> Int {
        let depth = depthHelper(root)
        if depth == -1 {
            return 0
        } else if depth == 0 {
            return 1
        }
        var (left, right) = (0, Int(pow(Double(2),Double(depth))) - 1)
        while left < right {
            let pivot: Int = left + (right - left)/2
            if nodeExists(root, depth, pivot) {
                left = pivot + 1
            } else {
                right = pivot - 1
            }
        }
        return Int(pow(Double(2),Double(depth))) - 1 + left
    }
    
    func depthHelper(_ root: TreeNode?) -> Int {
        var node = root
        var depth = -1
        while node != nil {
            depth += 1
            node = node!.left
        }
        return depth
    }
    
    func nodeExists(_ root: TreeNode?, _ depth: Int, _ pivot: Int) -> Bool {
        var root = root
        var (left, right) = (0, Int(pow(Double(2),Double(depth))) - 1)
        for i in 0...depth {
            var mid = left + (right - left) / 2
            if mid < pivot {
                left = mid + 1
                root = root?.right ?? nil
            } else {
                right = mid
                root = root?.left ?? nil
            }
        }
        return false ? root == nil : true
    }
}
