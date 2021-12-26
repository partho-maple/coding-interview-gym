class Solution {
    func minRemoveToMakeValid(_ s: String) -> String {
        var  indexes_to_remove: Set = Set<Int>()
        var stack: [Int] = []
        
        for (index, item) in s.enumerated() {
            if "()".contains(item) == false {
                continue
            }
            
            if item == "(" {
                stack.append(index)
            } else if item == ")" {
                if stack.count <= 0 {
                    indexes_to_remove.insert(index)
                } else {
                    stack.popLast()
                }
            }
        }
        indexes_to_remove = indexes_to_remove.union(Set(stack))
        var resultString = ""
        for (index, item) in s.enumerated() {
            if !indexes_to_remove.contains(index) {
                resultString += String(item)
            }
        }
        return resultString
    }
}



class Solution {
    func minRemoveToMakeValid(_ s: String) -> String {
        var sArray = Array(s), stack = [Character](), leftCount = 0, rightCount = 0

        for item in sArray {
            if item == "(" {
                stack.append(item)
                leftCount += 1
            } else if item == ")" {
                if leftCount > 0 {
                    stack.append(item)
                    leftCount -= 1
                }
            } else {
                stack.append(item)
            }
        }
        
        sArray = stack
        stack.removeAll()
        
        for item in sArray.reversed() {
            if item == "(" {
                if rightCount > 0 {
                    stack.append(item)
                    rightCount -= 1
                }
            } else if item == ")" {
                stack.append(item)
                rightCount += 1
            } else {
                stack.append(item)
            }
        }
        return stack.reversed().reduce("") { $0 + String($1) }
    }
}
