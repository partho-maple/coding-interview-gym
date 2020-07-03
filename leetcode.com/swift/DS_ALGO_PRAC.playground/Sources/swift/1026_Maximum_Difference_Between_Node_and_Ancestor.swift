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

// Brute force, Bottom-Up. Time: O(n^2)
class Solution {
    func maxAncestorDiff(_ root: TreeNode?) -> Int {
        var currentMaxDIff = 0
        maxAncestorDiffHelper(root, &currentMaxDIff)
        return currentMaxDIff
    }
    
    func maxAncestorDiffHelper(_ root: TreeNode?, _ currentMaxDIff: inout Int) -> [Int] {
        guard let node = root else {
            return []
        }
        let leftNodeVals = maxAncestorDiffHelper(node.left, &currentMaxDIff)
        let rightNodeVals = maxAncestorDiffHelper(node.right, &currentMaxDIff)
        let allVals = leftNodeVals + rightNodeVals
        for num in allVals {
            currentMaxDIff = max(currentMaxDIff, abs(node.val - num))
        }
        return allVals + [node.val]
    }
}


// Optimised. Time: O(n)
class Solution {
    func maxAncestorDiff(_ root: TreeNode?) -> Int {
        var currentMaxDIff = 0
        maxAncestorDiffHelper(root, &currentMaxDIff)
        return currentMaxDIff
    }
    
    func maxAncestorDiffHelper(_ root: TreeNode?, _ currentMaxDIff: inout Int) -> [Int] {
        guard let node = root else {
            return []
        }
        let leftNodeVals = maxAncestorDiffHelper(node.left, &currentMaxDIff)
        let rightNodeVals = maxAncestorDiffHelper(node.right, &currentMaxDIff)
        let allVals = leftNodeVals + rightNodeVals
        for num in allVals {
            currentMaxDIff = max(currentMaxDIff, abs(node.val - num))
        }
        return [(allVals + [node.val]).min()!, (allVals + [node.val]).max()!]
    }
}
