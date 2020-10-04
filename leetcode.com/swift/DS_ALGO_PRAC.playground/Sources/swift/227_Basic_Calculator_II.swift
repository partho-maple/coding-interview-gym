import Foundation
class Solution {
    func calculate(_ s: String) -> Int {
        var expression: [String] = Array(s).map { String($0) }.filter { $0 != " " }
        var (stack, currentSign, rightNum) = ([Int](), "+", 0)
        for (index, value) in expression.enumerated() {
            if let num = Int(value) {
                rightNum = rightNum * 10 + num
            }
            if (index == expression.count - 1) || ["+", "-", "*", "/"].contains(value) {
                if currentSign == "+" {
                    stack.append(rightNum)
                } else if currentSign == "-" {
                    stack.append(0 - rightNum)
                } else if currentSign == "*" {
                    let leftNum = stack.popLast()!
                    stack.append(leftNum * rightNum)
                } else {
                    let leftNum = stack.popLast()!
                    stack.append(leftNum / rightNum)
                }
                currentSign = value
                rightNum = 0
            }
        }
        return stack.reduce(0) { $0 + $1 }
    }
}
