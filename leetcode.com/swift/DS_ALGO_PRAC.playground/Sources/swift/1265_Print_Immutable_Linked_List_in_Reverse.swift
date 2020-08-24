/**
 * Definition for ImmutableListNode.
 * public class ImmutableListNode {
 *     public func printValue() {}
 *     public func getNext() -> ImmutableListNode? {}
 * }
 */

// Approach 1: Time O(n) , Space O(n)
class Solution {
    func printLinkedListInReverse(_ head: ImmutableListNode?) {
        guard let head = head else {
            return
        }
        printLinkedListInReverse(head.getNext())
        head.printValue()
    }
}
