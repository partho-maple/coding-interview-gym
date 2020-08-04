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
    func verticalTraversal(_ root: TreeNode?) -> [[Int]] {
        guard let root = root else {
            return [[]]
        }
        var nodeValMap = [String:[Int]]()
        var nodeQueue = Array([(root, 0, 0)])
        var (maxX, minX) = (Int.min,Int.max)
        var minY = Int.max
        while nodeQueue.count > 0 {
            var currentLevelLen = nodeQueue.count
            for _ in 0..<currentLevelLen {
                var (currNode, xCord, yCord) = nodeQueue.removeFirst()
                maxX = max(maxX, xCord)
                minX = min(minX, xCord)
                minY = min(minY, yCord)
                nodeValMap["\(xCord)#\(yCord)", default:[Int]()].append(currNode.val)
                if let left = currNode.left {
                    nodeQueue.append((left, xCord - 1, yCord - 1))
                }
                if let right = currNode.right {
                    nodeQueue.append((right, xCord + 1, yCord - 1))
                }
            }
        }
        var result = [[Int]]()
        for x in minX...maxX {
            var currentCol = [Int]()
            for y in stride(from: 0, through: minY, by: -1) {
                if let val = nodeValMap["\(x)#\(y)"] {
                    currentCol += val.sorted()
                }
            }
            result.append(currentCol)
        }
        return result
    }
}
