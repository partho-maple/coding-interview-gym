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
class Solution {
    func closestValue(_ root: TreeNode?, _ target: Double) -> Int {
        guard let root = root else {
            return Int(target)
        }
        
        if let left = root.left, target < Double(root.val) {
            let leftVal = closestValue(left, target)
            if abs(target - Double(leftVal)) < abs(target - Double(root.val)) {
                return leftVal
            } else {
                return root.val
            }
        } else if let right = root.right, target > Double(root.val) {
            let rightVal = closestValue(right, target)
            if abs(target - Double(rightVal)) < abs(target - Double(root.val)) {
                return rightVal
            } else {
                return root.val
            }
        } else {
            return root.val
        }
    }
}
