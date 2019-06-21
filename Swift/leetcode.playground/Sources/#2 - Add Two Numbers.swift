//: Playground - noun: a place where people can play

import UIKit

//: Problem:    https://leetcode.com/problems/add-two-numbers/




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
    
    public init() {
        
    }
    
    
    public func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var dummyHead = ListNode(0)
        var p:ListNode? = l1
        var q:ListNode? = l2
        var carry = 0
        var currentNode = dummyHead
        
        while ((p != nil) || (q != nil)) {
            let x:Int = p?.val ?? Int(0) // Doc: https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/BasicOperators.html
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


