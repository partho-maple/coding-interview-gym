class Solution {
    func canReorderDoubled(_ arr: [Int]) -> Bool {
        let sortedArray = arr.sorted { abs($0) < abs($1) }
        var counterMap = [Int:Int]()
        sortedArray.forEach { item in
            counterMap[item, default: 0] += 1
        }
        
        for item in sortedArray {
            if counterMap[item]! == 0 {
                continue
            } else {
                counterMap[item]! -= 1
            }
            if let counter = counterMap[2 * item] {
                if counter == 0 {
                    return false
                } else {
                    counterMap[2 * item]! -= 1
                }
            } else {
                return false
            }
        }
        return true
    }
}
