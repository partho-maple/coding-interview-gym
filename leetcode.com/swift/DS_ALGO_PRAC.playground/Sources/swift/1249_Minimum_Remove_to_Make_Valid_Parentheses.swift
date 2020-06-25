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
