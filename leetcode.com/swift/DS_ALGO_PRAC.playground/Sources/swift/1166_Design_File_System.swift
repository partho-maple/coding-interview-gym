
class FileSystem {

    var trie = Trie()
    init() {
        
    }
    
    func createPath(_ path: String, _ value: Int) -> Bool {
        return trie.insert(path, value)
    }
    
    func get(_ path: String) -> Int {
        return trie.contains(path)
    }
}

class TrieNode {
    var name: String
    var children: [String:TrieNode]
    var value: Int
    
    init(_ name: String, _ value: Int = -1, children: [String:TrieNode] = [:]) {
        self.name = name
        self.children = children
        self.value = value
    }
}

class Trie {
    var root: TrieNode
    
    init () {
        root = TrieNode("/")
    }
    
    func insert(_ path: String, _ value: Int) -> Bool {
        let pathComponents = path.split(separator: "/").map { String($0) }
        guard pathComponents.count > 0 else {
            return false
        }
        
        var currentNode = root
        for (_, item) in pathComponents.enumerated() {
            if currentNode.children[item] == nil {
                if item == pathComponents.last {
                    let newNode = TrieNode(item)
                    currentNode.children[item] = newNode
                } else {
                    return false
                }
            }
            currentNode = currentNode.children[item]!
        }
        
        if currentNode.value != -1 {
            return false
        } else {
            currentNode.value = value
            return true
        }
    }
    
    func contains(_ path: String) -> Int {
        let pathComponents = path.split(separator: "/").map { String($0) }
        guard pathComponents.count > 0 else {
            return -1
        }
        
        var currentNode = root
        for (_, item) in pathComponents.enumerated() {
            if let nextNode = currentNode.children[item] {
                currentNode = nextNode
            } else {
                return -1
            }
        }
        return currentNode.value
    }
}
