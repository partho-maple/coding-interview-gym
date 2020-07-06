import Foundation
class Solution {
    func addStrings(_ num1: String, _ num2: String) -> String {
        var digits1: [Int] = num1.compactMap { $0.wholeNumberValue }
        var digits2: [Int] = num2.compactMap { $0.wholeNumberValue }
        var carry = 0
        var resultStack: [Int] = []
        while digits1.count > 0 || digits2.count > 0 {
            var (digit1, digit2) = (0, 0)
            if digits1.count > 0 {
                digit1 = digits1.popLast()!
            }
            if digits2.count > 0 {
                digit2 = digits2.popLast()!
            }
            let sum = digit1 + digit2 + carry
            let remainder = sum % 10
            carry = sum / 10
            resultStack.append(remainder)
        }
        if carry > 0 {
            resultStack.append(carry)
        }
        resultStack = resultStack.reversed()
        return resultStack.reduce("", { $0 + String($1)})
    }
}
