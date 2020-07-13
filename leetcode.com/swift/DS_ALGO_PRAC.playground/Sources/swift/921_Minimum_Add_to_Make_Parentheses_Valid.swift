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
