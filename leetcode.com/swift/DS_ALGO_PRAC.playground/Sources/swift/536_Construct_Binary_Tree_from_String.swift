import Foundation

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil; }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func str2tree(_ s: String) -> TreeNode? {
        guard s.count > 0, var str: [Character] = Array(s) else {
            return nil
        }
        var currentIndex = 0
        return str2treeDFSHelper(str, &currentIndex)
    }
    
    private func str2treeDFSHelper(_ strArr: [Character], _ currentIndec: inout Int) -> TreeNode? {
        guard currentIndec < strArr.count else {
            return nil
        }
        
        print("Index:   \(currentIndec), value:   \(strArr[currentIndec].wholeNumberValue)")
        var currentNodeVal: Int = strArr[currentIndec].wholeNumberValue!
        currentIndec += 1
        while currentIndec < strArr.count {
            if strArr[currentIndec].isWholeNumber {
                currentNodeVal = currentNodeVal*10 + strArr[currentIndec].wholeNumberValue!
                currentIndec += 1
            } else {
                break
            }
        }
        
        var currentNode: TreeNode = TreeNode(currentNodeVal)
        if String(strArr[currentIndec]) == "(" {
            currentIndec += 1
            var left: TreeNode? = str2treeDFSHelper(strArr, &currentIndec)
            currentNode.left = left
            
            currentIndec += 1
            var right: TreeNode? = str2treeDFSHelper(strArr, &currentIndec)
            currentNode.right = right
        } else if String(strArr[currentIndec]) == ")" {
            return currentNode
        }
        
        
        return currentNode
    }
}
