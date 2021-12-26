import Foundation
class Solution {
    func minAddToMakeValid(_ S: String) -> Int {
        var stack = [String]()
        for char in S {
            let charStr = String(char)
            
            if stack.isEmpty {
                stack.append(charStr)
            } else if charStr == ")" && stack.last! == "(" {
                stack.popLast()
            } else {
                stack.append(charStr)
            }
        }
        return stack.count
    }
}


class Solution {
    func minAddToMakeValid(_ s: String) -> Int {
        var stack = [Character](), count = 0
        for char in s {
            if char == Character("(") {
                stack.append(char)
            } else if char == Character(")") {
                if !stack.isEmpty && stack.last! == Character("(") {
                    stack.removeLast()
                } else {
                    count += 1
                }
            }
        }
        return count + stack.count
    }
}
