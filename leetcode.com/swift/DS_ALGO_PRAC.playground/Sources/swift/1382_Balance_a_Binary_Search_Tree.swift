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
    func balanceBST(_ root: TreeNode?) -> TreeNode? {
        var sortedNodeVals = [Int]()
        inorderDFS(root, &sortedNodeVals)
        return balanceBST_HelperDFS(sortedNodeVals)
    }
    
    func inorderDFS(_ root: TreeNode?, _ array: inout [Int] ) {
        guard let root = root else {
            return
        }
        inorderDFS(root.left, &array)
        array.append(root.val)
        inorderDFS(root.right, &array)
    }
    
    func balanceBST_HelperDFS(_ sortedArray: [Int] ) -> TreeNode? {
        guard sortedArray.count > 0 else {
            return nil
        }
        let mid = sortedArray.count / 2
        let root = TreeNode(sortedArray[mid])
        root.left = balanceBST_HelperDFS(Array(sortedArray[0..<mid]))
        root.right = balanceBST_HelperDFS(Array(sortedArray[(mid + 1)..<sortedArray.count]))
        return root
    }
}
