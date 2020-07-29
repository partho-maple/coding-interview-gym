
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
    func diameterOfBinaryTree(_ root: TreeNode?) -> Int {
        var diameter = 0
        diameterOfBinaryTreeDFSHelper(root, &diameter)
        return diameter
    }
    
    private func diameterOfBinaryTreeDFSHelper(_ root: TreeNode?, _ diameter: inout Int) -> Int {
        guard let root = root else {
            return 0
        }
        let leftmaxDepth = diameterOfBinaryTreeDFSHelper(root.left, &diameter)
        let rightmaxDepth = diameterOfBinaryTreeDFSHelper(root.right, &diameter)
        
        diameter = max(diameter, leftmaxDepth + rightmaxDepth)
        
        return max(leftmaxDepth, rightmaxDepth) + 1
    }
}
