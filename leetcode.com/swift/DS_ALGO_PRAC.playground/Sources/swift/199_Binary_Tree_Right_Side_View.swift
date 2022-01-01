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

// DFS
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


// BFS with level size measurement
class Solution {
    func rightSideView(_ root: TreeNode?) -> [Int] {
        guard let root = root else {
            return []
        }
        var result = [Int](), queue = [TreeNode](), currentLevelLength = 1
        queue.append(root)
        while !queue.isEmpty {
            var rightMostNode = Int.min, currentLevelLength = queue.count
            while currentLevelLength > 0 {
                let node = queue.removeFirst()
                rightMostNode = node.val
                currentLevelLength -= 1
                if let left = node.left {
                    queue.append(left)
                }
                if let right = node.right {
                    queue.append(right)
                }
            }
            result.append(rightMostNode)
        }
        return result
    }
}
