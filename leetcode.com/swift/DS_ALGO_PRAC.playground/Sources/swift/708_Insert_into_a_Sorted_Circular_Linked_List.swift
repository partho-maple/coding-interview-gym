import Foundation
// Source: https://tinyurl.com/y4p9krj8
class Solution {
    func insert(_ head: Node?, _ insertVal: Int) -> Node? {
        guard var head = head else {
            var node = Node(insertVal)
            node.next = node
            return node
        }
        var current: Node = head.next!
        var previous: Node = head
        var toInsertHere = false
        while true {
            if (previous.val <= insertVal && insertVal <= current.val) {
                // Case 1, usual scenerio
                toInsertHere = true
            } else if previous.val > current.val {
                // Case 2, where we locate the tail element, 'previous' points  to tails as the largest element
                if insertVal >= previous.val || insertVal <= current.val {
                    toInsertHere = true
                }
            }
            
            if toInsertHere {
                var target = Node(insertVal)
                target.next = current
                previous.next = target
                return head
            }
            previous = current
            current = current.next!
            if previous == head {
                break
            }
        }
        
        // Case 3, did not insetr the node in the loop
        var target = Node(insertVal)
        target.next = current
        previous.next = target
        return head
    }
}
