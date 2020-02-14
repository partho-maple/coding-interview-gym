import Foundation

class Solution {
    func evalRPN(_ tokens: [String]) -> Int {
        var opes = ["+", "-", "*", "/"]
        var stack = [String]()
        for token in tokens {
            if opes.contains(token)  {
                var rightOperand: Double! = Double(stack.popLast()!)
                var leftOperand: Double! = Double(stack.popLast()!)
                var result = 0.0
                if token == "+" {
                    result = leftOperand + rightOperand
                } else if token == "-" {
                    result = leftOperand - rightOperand
                } else if token == "*" {
                    result = leftOperand * rightOperand
                } else {
                    if (rightOperand*leftOperand < 0) && (Int(leftOperand)%Int(rightOperand) != 0) {
                        result = leftOperand / rightOperand + 1
                    } else {
                        result = leftOperand / rightOperand
                    }
                }
                var res = Int(result.round(.towardZero)
                stack.append(String(res))
            } else {
                stack.append(token)
            }
        }
        print("stack: \(stack)")
        return Int(stack.popLast()!)!
    }
}
