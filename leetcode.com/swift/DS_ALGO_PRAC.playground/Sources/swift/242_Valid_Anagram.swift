import Foundation

class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        guard (s.count == t.count) else {
            return false
        }
        var sDict = [Character:Int]()
        var tDict = [Character:Int]()
        for char in s {
            if let count = sDict[char] {
                sDict[char]! += 1
            } else {
                sDict[char] = 1
            }
        }
        for char in t {
            if let count = tDict[char] {
                tDict[char]! += 1
            } else {
                tDict[char] = 1
            }
        }
        return sDict == tDict
    }
}
