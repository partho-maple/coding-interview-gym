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
    func sumNumbers(_ root: TreeNode?) -> Int {
        guard let node = root else {
            return 0
        }

        var currentPath = [node.val]
        var currentSum = 0
        sumNumbersHelper(node, &currentPath, &currentSum)
        return currentSum
    }
    
    func sumNumbersHelper(_ root: TreeNode?, _ currentPath: inout [Int], _ currentSum: inout Int) -> Void {
        guard let node = root else {
            return
        }
        if isLeaf(node) {
            if let pathSum = Int(currentPath.reduce("", {$0 + String($1)})) {
                currentSum += pathSum
            }
            return
        }
        
        if let left = node.left {
            currentPath.append(left.val)
            sumNumbersHelper(left, &currentPath, &currentSum)
            currentPath.popLast()
        }
        if let right = node.right {
            currentPath.append(right.val)
            sumNumbersHelper(right, &currentPath, &currentSum)
            currentPath.popLast()
        }
    }
    
    func isLeaf(_ node: TreeNode) -> Bool {
        return node.left == nil && node.right == nil
    }
}


// Second try
class Solution {
    func sumNumbers(_ root: TreeNode?) -> Int {
        var currentPath = [Int](), currentSum = 0
        sumNumbersDFSHelper(root, currentPath, &currentSum)
        return currentSum
    }

    func sumNumbersDFSHelper(_ root: TreeNode?, _ currentPath: [Int], _ currentSum: inout Int) {
        guard let root = root else {
            return
        }

        if root.left == nil && root.right == nil {
            let currentPath = currentPath + [root.val]
            let currentNumStr = currentPath.reduce("") { $0 + String($1) }
            let currentNum = Int(currentNumStr)
            currentSum += currentNum!
        }
        if let left = root.left {
            sumNumbersDFSHelper(left, currentPath + [root.val], &currentSum)
        }
        if let right = root.right {
            sumNumbersDFSHelper(right, currentPath + [root.val], &currentSum)
        }
    }
}
