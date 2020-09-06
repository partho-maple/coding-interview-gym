/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func str2tree(_ s: String) -> TreeNode? {
        var sArr: [Character] = Array(s)
        var currentIndex = 0
        return str2treeDFSHelper(sArr, &currentIndex)
    }
    
    func str2treeDFSHelper(_ s: [Character], _ currentIndex: inout Int) -> TreeNode? {
        var node: TreeNode?
        
        if currentIndex < s.count && s[currentIndex] != ")"{
            if s[currentIndex] == "(" {
                currentIndex += 1
            }
            
            var isNegative = false
            if s[currentIndex] == "-" {
                isNegative = true
                currentIndex += 1
            }

            var nodeVal = [Character]()
            while currentIndex < s.count && s[currentIndex].isNumber  {
                nodeVal.append(s[currentIndex])
                currentIndex += 1
            }

            if let nodeValInt = Int(nodeVal.reduce("") { $0 + String($1) }) {
                if isNegative {
                    node = TreeNode((0 - nodeValInt))
                } else {
                    node = TreeNode(nodeValInt)
                }
                
                if currentIndex < s.count && s[currentIndex] == "(" {
                    currentIndex += 1
                    node?.left = str2treeDFSHelper(s, &currentIndex)
                }
                
                if currentIndex < s.count && s[currentIndex] == "(" {
                    currentIndex += 1
                    node?.right = str2treeDFSHelper(s, &currentIndex)
                }
                
                if currentIndex >= s.count || s[currentIndex] == ")" {
                    currentIndex += 1
                    return node
                }
            }
        }
        return node
    }
}
