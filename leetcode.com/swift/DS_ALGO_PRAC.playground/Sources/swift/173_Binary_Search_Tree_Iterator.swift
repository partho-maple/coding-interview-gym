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

class BSTIterator {

    var nodeStack = [TreeNode]()
    
    init(_ root: TreeNode?) {
        var currentNode: TreeNode? = root
        while var node = currentNode  {
            nodeStack.append(node)
            currentNode = node.left
        }
    }
    
    /** @return the next smallest number */
    func next() -> Int {
        if var currentNode = nodeStack.popLast() {
            let valToReturn = currentNode.val
            if let right = currentNode.right {
                nodeStack.append(right)
                currentNode = right
                while let node = currentNode.left  {
                    nodeStack.append(node)
                    currentNode = node
                }
            }
            return valToReturn
        } else {
            return -1
        }
    }
    
    /** @return whether we have a next smallest number */
    func hasNext() -> Bool {
        return nodeStack.count > 0 ? true : false
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * let obj = BSTIterator(root)
 * let ret_1: Int = obj.next()
 * let ret_2: Bool = obj.hasNext()
 */
