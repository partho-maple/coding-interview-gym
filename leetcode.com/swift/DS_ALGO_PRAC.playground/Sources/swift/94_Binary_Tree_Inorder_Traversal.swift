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
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        var result = [Int]()
        var stack = [TreeNode?]()
        var currentNode = root
        while !stack.isEmpty || currentNode != nil {
            if currentNode != nil {
                stack.append(currentNode)
                currentNode = currentNode?.left
            } else {
                if let node = stack.removeLast() {
                    result.append(node.val)
                    currentNode = node.right
                }
            }
        }
        return result
    }
}


/*
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, result = [], []
        currentNode = root
        while currentNode is not None or len(stack) > 0:
            if currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.left
            else:
                currentNode = stack.pop()
                result.append(currentNode.val)
                currentNode = currentNode.right
        return result
*/
