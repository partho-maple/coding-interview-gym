import Foundation
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

class Codec {
    func serialize(_ root: TreeNode?) -> String {
        var preorderSequence = [String]()
        var nodeStack = [TreeNode]()
        var currentNode = root
        while true {
            if let current = currentNode  {
                preorderSequence.append(String(current.val) + ",")
                nodeStack.append(current)
                currentNode = current.left
            } else {
                if nodeStack.count <= 0 {
                    break
                }
                preorderSequence.append("X,")
                currentNode = nodeStack.popLast()
                currentNode = currentNode!.right
            }
        }
        return preorderSequence.reduce("", {$0 + $1})
    }
    
    func deserialize(_ data: String) -> TreeNode? {
        guard !data.isEmpty else {
            return nil
        }
        var nodeValueQueue = data.split(separator: ",")
        var treeNodeStack = [TreeNode]()
        var head: TreeNode?
        var currentNode: TreeNode?
        var isLeft = true
        while nodeValueQueue.count > 0 {
            let nodeVal = nodeValueQueue.removeFirst()
            if nodeVal == "X" {
                var node = treeNodeStack.popLast()
                currentNode = node
                isLeft = false
            } else {
                var node = TreeNode(Int(nodeVal)!)
                if currentNode != nil {
                    if isLeft {
                        currentNode!.left = node
                    } else {
                        currentNode!.right = node
                        isLeft = true
                    }
                } else {
                    head = node
                }
                currentNode = node
                treeNodeStack.append(node)
            }
        }
        return head
    }
}

// Your Codec object will be instantiated and called as such:
// var codec = Codec()
// codec.deserialize(codec.serialize(root))
