class Solution {
    func calculate(_ s: String) -> Int {
        let sArray = Array(s)
        var stack = [String](), currentNumber = [Character]()
        for item in sArray {
            if item.isNumber {
                currentNumber.append(item)
            } else if !currentNumber.isEmpty {
                let number = currentNumber.map { String($0) }.reduce("") { $0 + $1 }
                stack.append(number)
                currentNumber.removeAll()
            }
            if item == " " {
                continue
            }
            if item == "+" || item == "-" || item == "(" {
                stack.append(String(item))
            }
            if item == ")" {
                var subExp = [String]()
                while stack.last! != "(" {
                    subExp.append(stack.removeLast())
                }
                stack.removeLast() // removes last "(" character
                let currentValue = evalExpression(subExp.reversed())
                stack.append(String(currentValue)) // Adds back the calculated number
            }
        }
        
        if !currentNumber.isEmpty {
            let number = currentNumber.map { String($0) }.reduce("") { $0 + $1 }
            stack.append(number)
            currentNumber.removeAll()
        }
        return evalExpression(stack)
    }
    
    func evalExpression(_ exp: [String]) -> Int {
        var prevNumber = 0, prevSign = "+"
        for item in exp {
            if item == "+" || item == "-" {
                prevSign = item
                continue
            }
            
            var newNum = 0
            if prevSign == "+" {
                newNum = Int(prevNumber) + Int(item)!
            } else {
                newNum = Int(prevNumber) - Int(item)!
            }
            prevNumber = newNum
        }
        return prevNumber
    }
}
