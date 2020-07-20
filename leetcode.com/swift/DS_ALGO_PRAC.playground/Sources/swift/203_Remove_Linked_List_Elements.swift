public class ListNode {
   public var val: Int
   public var next: ListNode?
   public init() { self.val = 0; self.next = nil; }
   public init(_ val: Int) { self.val = val; self.next = nil; }
   public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}

import Foundation
class Solution {
   func removeElements(_ head: ListNode?, _ val: Int) -> ListNode? {
       var dummyHead = ListNode(Int.max, head)
       var prev: ListNode?
       var current: ListNode? = dummyHead
       while current != nil {
           if current!.val == val {
               prev?.next = current?.next
           } else {
               prev = current
           }
           current = current?.next
       }
       return dummyHead.next
   }
}
