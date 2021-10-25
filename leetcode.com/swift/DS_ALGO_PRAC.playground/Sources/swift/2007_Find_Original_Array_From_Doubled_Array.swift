import Foundation
class Solution {
    func findOriginalArray(_ changed: [Int]) -> [Int] {
        guard changed.count % 2 == 0 else { return [] }
        let changedSorted = changed.sorted()
        var countMap = [Int:Int]()
        changed.forEach { item in
            countMap[item, default: 0] += 1
        }
        var original = [Int]()
        for item in changedSorted {
            let key = item * 2
            if let _ = countMap[key],
               let _ = countMap[item] {
                countMap[key]! -= 1
                countMap[item]! -= 1
                original.append(item)
                if let count = countMap[key], count == 0 {
                    countMap.removeValue(forKey:key)
                }
                if let count = countMap[item], count == 0 {
                    countMap.removeValue(forKey:item)
                }
            }
        }
        if countMap.keys.count == 0 && original.count * 2 == changed.count {
            return original
        } else {
            return []
        }
    }
}
