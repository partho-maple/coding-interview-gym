import Foundation

class TreeNode {
    let start: Int
    let end: Int
    var left: TreeNode?
    var right: TreeNode?
    
    init(_ start: Int, _ end: Int) {
        self.start = start
        self.end = end
    }
}

class MyCalendar {

    var root: TreeNode?
    
    init() {
        
    }
    
    func bookHelper(_ start: Int, _ end: Int, _ node: inout TreeNode) -> Bool {
        if start >= node.end {
            if node.right != nil {
                return self.bookHelper(start, end, &node.right!)
            } else {
                node.right = TreeNode(start, end)
                return true
            }
        } else if end <= node.start {
            if node.left != nil {
                return self.bookHelper(start, end, &node.left!)
            } else {
                node.left = TreeNode(start, end)
                return true
            }
        } else {
            return false
        }
    }
    
    func book(_ start: Int, _ end: Int) -> Bool {
        if let root = self.root {
            return self.bookHelper(start, end, &self.root!)
        }
        self.root = TreeNode(start, end)
        return true
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * let obj = MyCalendar()
 * let ret_1: Bool = obj.book(start, end)
 */
