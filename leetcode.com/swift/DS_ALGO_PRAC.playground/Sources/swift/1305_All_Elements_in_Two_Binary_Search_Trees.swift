import Foundation

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil; }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

// Iterative inorder DFS
class Solution {
    func getAllElements(_ root1: TreeNode?, _ root2: TreeNode?) -> [Int] {
        var (result, stack1, stack2) = ([Int](), [TreeNode](), [TreeNode]())
        var (currentNode1, currentNode2) = (root1, root2)
        
        while (!stack1.isEmpty || currentNode1 != nil) || (!stack2.isEmpty || currentNode2 != nil) {
            while let node1 = currentNode1 {
                stack1.append(node1)
                currentNode1 = node1.left
            }
            
            while let node2 = currentNode2 {
                stack2.append(node2)
                currentNode2 = node2.left
            }
            
            if stack2.isEmpty || !stack1.isEmpty && (stack2.last!.val >= stack1.last!.val) {
                currentNode1 = stack1.removeLast()
                result.append(currentNode1!.val)
                currentNode1 = currentNode1!.right
            } else {
                currentNode2 = stack2.removeLast()
                result.append(currentNode2!.val)
                currentNode2 = currentNode2!.right
            }
        }
        return result
    }
}
