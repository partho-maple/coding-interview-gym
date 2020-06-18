// Definition for singly-linked list.
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}


public class Solution_2 {
    public func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var dummyHead = ListNode(0)
        var p:ListNode? = l1
        var q:ListNode? = l2
        var carry = 0
        var currentNode = dummyHead
        
        while ((p != nil) || (q != nil)) {
            let x:Int = p?.val ?? Int(0) 
            let y:Int = q?.val ?? Int(0)
            let sum = x + y + carry
            carry = sum/10
            currentNode.next = ListNode(sum%10)
            currentNode = currentNode.next!
            
            if (p != nil) {
                p = p?.next
            }
            
            if (q != nil) {
                q = q?.next
            }
        }
        
        if carry > 0 {
            currentNode.next = ListNode(carry)
        }
        
        return dummyHead.next
    }
}





/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */
class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        
    }
}
