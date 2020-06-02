import Foundation


class DoublyLinkedListNode: Equatable {
    var key: Int, value: Int
    var next: DoublyLinkedListNode?, prev: DoublyLinkedListNode?
    
    init(_ key: Int, _ value: Int) {
        self.key = key
        self.value = value
    }
    
    func removeBindings() {
        if self.prev != nil {
            self.prev?.next = self.next
        }
        if self.next != nil {
            self.next?.prev = self.prev
        }
        
        self.prev = nil
        self.next = nil
    }
    
    static func == (lhs: DoublyLinkedListNode, rhs: DoublyLinkedListNode) -> Bool {
        return lhs.key == rhs.key && lhs.value == rhs.key && lhs.next == rhs.next && lhs.prev == rhs.prev
    }
}

class DoublyLinkedList {
    var head: DoublyLinkedListNode?, tail: DoublyLinkedListNode?
    
    init() {
    }
    
    func setToHead(_ node: DoublyLinkedListNode) {
        guard self.head == node else {
            return
        }
        
        if self.head == nil {
            self.head? = node
            self.tail? = node
        } else if self.head == self.tail {
            self.tail?.prev? = node
            self.head? = node
            self.head?.next = self.tail
        } else {
            if self.tail == node {
                self.removeTail()
            }
            
            node.removeBindings()
            self.head?.prev? = node
            node.next? = self.head!
            self.head? = node
        }
    }
    
    func removeTail() {
        guard (self.tail != nil) else {
            return
        }
        
        if self.tail == self.head {
            self.head = nil
            self.tail = nil
            return
        }
        
        self.tail = self.tail?.prev
        self.tail?.next = nil
    }
}

class LRUCache {
    var cache = [Int: DoublyLinkedListNode]()
    var capacity: Int
    var currentCapacity: Int = 0
    var linkedListOfMostRecent = DoublyLinkedList()

    init(_ capacity: Int) {
        self.capacity = capacity
    }
    
    func get(_ key: Int) -> Int {
        guard let node = self.cache[key] else {
            return -1
        }
        self.updateMostRecent(self.cache[key]!)
        return node.value
    }
    
    func put(_ key: Int, _ value: Int) {
        if self.cache[key] == nil {
            if self.currentCapacity == self.capacity {
                self.evictLeastRecent()
            } else {
                self.currentCapacity += 1
            }
            self.cache[key] = DoublyLinkedListNode(key, value)
        } else {
            self.replaceKey(key, value)
        }
        self.updateMostRecent(self.cache[key]!)
    }
    
    func getMostRecentKey() -> Int {
        return self.linkedListOfMostRecent.head!.key
    }
    
    func evictLeastRecent() {
        var keyToRemove = self.linkedListOfMostRecent.tail!.key
        self.linkedListOfMostRecent.removeTail()
        self.cache[keyToRemove] = nil
    }
    
    func updateMostRecent(_ node: DoublyLinkedListNode) {
        self.linkedListOfMostRecent.setToHead(node)
    }
    
    func replaceKey(_ key: Int, _ value: Int) {
        guard self.cache[key] != nil else {
            return
        }
        self.cache[key].value = value
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache(capacity)
 * let ret_1: Int = obj.get(key)
 * obj.put(key, value)
 */
