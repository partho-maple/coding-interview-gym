import Foundation

// Definition for a Node.
public class Node {
    public var val: Int
    public var left: Node?
    public var right: Node?
    public init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
}

import Foundation
class Solution {
    func treeToDoublyList(_ root: Node?) -> Node? {
        guard let rootNode = root else {
            return root
        }
        var dummyHead = Node(Int.max)
        var dummyTail = Node(Int.max)
        treeToDoublyListInorderDFSHelper(rootNode, &dummyHead.right, &dummyTail.left)
        dummyHead.right!.left = dummyTail.left
        dummyTail.left!.right = dummyHead.right
        return dummyHead.right
    }
    
    private func treeToDoublyListInorderDFSHelper(_ root: Node?, _ listHead: inout Node? , _ listTail: inout Node?) {
        guard let rootNode = root else {
            return
        }
        treeToDoublyListInorderDFSHelper(rootNode.left, &listHead, &listTail)
        if var tail = listTail {
            tail.right = rootNode
            rootNode.left = tail
        } else {
            listHead = rootNode
        }
        listTail = rootNode
        treeToDoublyListInorderDFSHelper(rootNode.right, &listHead, &listTail)
     }
}
