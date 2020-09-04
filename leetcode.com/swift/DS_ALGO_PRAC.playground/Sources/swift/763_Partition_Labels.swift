import Foundation
class Solution {
    func partitionLabels(_ S: String) -> [Int] {
        guard S.count > 0 else {
            return []
        }
        var counter = [Character:Int]()
        let sArr = Array(S)
        sArr.forEach { char in
            counter[char, default: 0] += 1
        }
        
        var result = [Int]()
        var (left, right) = (0, 0)
        var windowCharSet = Set<Character>()
        while right < sArr.count {
            let currentChar = sArr[right]
            windowCharSet.insert(currentChar)
            counter[currentChar] = counter[currentChar]! - 1
            
            if counter[currentChar] == 0 {
                counter.removeValue(forKey: currentChar)
                windowCharSet.remove(currentChar)
            }
            
            if windowCharSet.count <= 0 {
                result.append(right - left + 1)
                left = right + 1
            }
            right += 1
        }
        return result
    }
}
