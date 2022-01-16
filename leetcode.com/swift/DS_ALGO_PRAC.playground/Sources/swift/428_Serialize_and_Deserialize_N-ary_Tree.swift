/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var children: [Node]
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.children = []
 *     }
 * }
 */

class Codec {
    func serialize(_ root: Node?) -> String {
        var nodeList = [Int]()
        serializeDFSHelper(root, &nodeList)
        let encodedString = nodeList.reduce("") { $0 + "," + String($1) }
        return encodedString
    }
    
    func serializeDFSHelper(_ root: Node?, _ nodeList: inout [Int]) {
        guard let root = root else {
            return
        }
        nodeList.append(root.val)
        nodeList.append(root.children.count)
        for child in root.children {
            serializeDFSHelper(child, &nodeList)
        }
    }
    
    func deserialize(_ data: String) -> Node? {
        let nodeList = data.components(separatedBy: ",").flatMap { Int($0) }
        guard nodeList.count > 0 else {
            return nil
        }
        var currentIndex = 0
        return deserializeDFSHelper(nodeList, &currentIndex)
    }
    
    func deserializeDFSHelper(_ nodeList: [Int], _ currentIndex: inout Int) -> Node? {
        guard currentIndex + 1 < nodeList.count else {
            return nil
        }
        let node = Node(nodeList[currentIndex]), childrenCount = nodeList[currentIndex + 1]
        currentIndex += 2
        if childrenCount == 0 {
            return node
        }
        
        var children = [Node]()
        for i in 0..<childrenCount {
            let child = deserializeDFSHelper(nodeList, &currentIndex)
            children.append(child!)
        }
        node.children = children
        return node
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let obj = Codec()
 * let ret_1: TreeNode? = obj.serialize(root)
 * let ret_2: Node? = obj.decode(data)
 */
