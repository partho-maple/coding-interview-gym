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
    func rangeSumBST(_ root: TreeNode?, _ L: Int, _ R: Int) -> Int {
        guard let node = root else {
            return 0
        }
        var (leftSum, rightSum, totalSum) = (0, 0, 0)
        
        if node.val >= L && node.val <= R {
            leftSum = rangeSumBST(node.left, L, R)
            rightSum = rangeSumBST(node.right, L, R)
            totalSum = leftSum + node.val + rightSum
        } else if node.val < L {
            rightSum = rangeSumBST(node.right, L, R)
            totalSum = rightSum
        } else if node.val > R {
            leftSum = rangeSumBST(node.left, L, R)
            totalSum = leftSum
        }
        return totalSum
    }
}
