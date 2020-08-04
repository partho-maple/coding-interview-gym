
// Brute force approach | Time O(n^2) | TLE : 34 / 36 test cases passed.
import Foundation
class Solution {
    func findAnagrams(_ s: String, _ p: String) -> [Int] {
        var pMap = [Character:Int]()
        for char in p {
            pMap[char, default: 0] += 1
        }
        let sArr = Array(s)
        var result = [Int]()
        for start in 0..<sArr.count {
            var need = pMap
            for i in start..<sArr.count {
                let curChar = sArr[i]
                if var needVal = need[curChar], needVal > 0 {
                    needVal -= 1
                    if needVal == 0 {
                        need.removeValue(forKey: curChar)
                        if need.keys.count <= 0 {
                            result.append(start)
                            break
                        }
                    } else {
                        need[curChar] = needVal
                    }
                } else {
                    break
                }
            }
        }
        return result
    }
}

// Sliding window | Time O(n)
class Solution {
    func findAnagrams(_ s: String, _ p: String) -> [Int] {
        if s.count < p.count {
            return []
        }
        let sArr = Array(s)
        var result = [Int]()
        var (pCounter, sCounter) = ([Character:Int](), [Character:Int]())
        for char in p {
            pCounter[char, default: 0] += 1
        }
        for i in 0..<(p.count - 1) {
            sCounter[sArr[i], default: 0] += 1
        }
        
        for right in (p.count - 1)..<sArr.count {
            let rightChar = sArr[right]
            sCounter[rightChar, default: 0] += 1
            if sCounter == pCounter {
                result.append(right - (p.count - 1))
            }
            let leftChar = sArr[right - (p.count - 1)]
            if var prevVal = sCounter[leftChar] {
                sCounter[leftChar] = prevVal - 1
                if sCounter[leftChar] == 0 {
                    sCounter.removeValue(forKey:leftChar)
                }
            }
        }
        return result
    }
}
