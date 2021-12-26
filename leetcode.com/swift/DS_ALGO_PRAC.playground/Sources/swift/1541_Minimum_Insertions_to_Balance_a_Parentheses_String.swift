class Solution {
    func minInsertions(_ s: String) -> Int {
        let sArray = Array(s)
        var stack = [Int](), result = 0
        for item in sArray {
            if item == "(" {
                if let last = stack.last {
                    if last == 2 {
                        stack.append(2)
                    } else {
                        result += 1
                        stack.removeLast()
                        stack.append(2)
                    }
                } else {
                    stack.append(2)
                }
            } else {
                if let last = stack.last {
                    if last == 2 {
                        stack.removeLast()
                        stack.append(1)
                    } else {
                        stack.removeLast()
                    }
                } else {
                    result += 1
                    stack.append(1)
                }
            }
        }
        result += stack.reduce(0) { $0 + $1 }
        return result
    }
}
