import Foundation
// Source: https://tinyurl.com/y2ame7dc
public class DoublyLinkedListNode {
    public var counterValKeySet = Set<String>()
    public var next: DoublyLinkedListNode?
    public var prev: DoublyLinkedListNode?
}

public class DoublyLinkedList {
    public var dummyHead = DoublyLinkedListNode()
    public var dummyTail = DoublyLinkedListNode()
    public init() {
        dummyHead.next = dummyTail
        dummyTail.prev = dummyHead
    }
    
    public func insertAfter(_ node: DoublyLinkedListNode) -> DoublyLinkedListNode {
        var (nodeToReturn, tempNode) = (DoublyLinkedListNode(), node.next)
        node.next = nodeToReturn
        nodeToReturn.prev = node
        nodeToReturn.next = tempNode
        tempNode?.prev = nodeToReturn
        return nodeToReturn
    }
    
    public func insertBefore(_ node: DoublyLinkedListNode) -> DoublyLinkedListNode {
        return insertAfter(node.prev!)
    }
    
    public func removeNode(_ node: DoublyLinkedListNode) {
        node.prev?.next = node.next
        node.next?.prev = node.prev
    }
}

class AllOne {
    var keyCounterToNodeMap = [Int: DoublyLinkedListNode]()
    var keyToCounterMap = [String: Int]()
    var dll = DoublyLinkedList()
    
    /** Initialize your data structure here. */
    init() {
        keyCounterToNodeMap[0] = dll.dummyHead
    }
    
    
    private func removePreviousKeyAndNode(_ previousCount: Int, _ key: String) {
        if var previousNode = keyCounterToNodeMap[previousCount] {
            previousNode.counterValKeySet.remove(key)
            if previousNode.counterValKeySet.isEmpty {
                dll.removeNode(previousNode)
                keyCounterToNodeMap.removeValue(forKey: previousCount)
            }
        }
    }
    
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    func inc(_ key: String) {
        keyToCounterMap[key, default:0] += 1
        let (currentCount, previousCount) = (keyToCounterMap[key]!, keyToCounterMap[key]! - 1)
        if keyCounterToNodeMap[currentCount] == nil {
            keyCounterToNodeMap[currentCount] = dll.insertAfter(keyCounterToNodeMap[previousCount]!)
        }
        keyCounterToNodeMap[currentCount]?.counterValKeySet.insert(key)
        if previousCount > 0 {
            removePreviousKeyAndNode(previousCount, key)
        }
    }
    
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    func dec(_ key: String) {
        if let previousCount = keyToCounterMap[key] {
            keyToCounterMap[key] = previousCount - 1
            if let currentCounter = keyToCounterMap[key] {
                if currentCounter == 0 {
                    keyToCounterMap.removeValue(forKey: key)
                } else {
                    if keyCounterToNodeMap[currentCounter] == nil {
                        keyCounterToNodeMap[currentCounter] = dll.insertBefore(keyCounterToNodeMap[previousCount]!)
                    }
                    keyCounterToNodeMap[currentCounter]?.counterValKeySet.insert(key)
                }
            }
            removePreviousKeyAndNode(previousCount, key)
        }
    }
    
    /** Returns one of the keys with maximal value. */
    func getMaxKey() -> String {
        if dll.dummyTail.prev!.counterValKeySet.count > 0 {
            return dll.dummyTail.prev!.counterValKeySet.first ?? ""
        } else {
            return ""
        }
    }
    
    /** Returns one of the keys with Minimal value. */
    func getMinKey() -> String {
        if dll.dummyHead.next!.counterValKeySet.count > 0 {
            return dll.dummyHead.next!.counterValKeySet.first ?? ""
        } else {
            return ""
        }
    }
}
