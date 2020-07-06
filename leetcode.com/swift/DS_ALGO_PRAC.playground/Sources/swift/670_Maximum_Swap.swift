import Foundation
// Time: O(nlogn)
class Solution {
    func maximumSwap(_ num: Int) -> Int {
        var digits: [Int] = String(num).compactMap{ $0.wholeNumberValue }
        let sortedDigits: [Int] = digits.sorted {$0 > $1}
        var numIdxMap = [Int:Int]()
        for (idx, item) in digits.enumerated() {
            numIdxMap[item] = idx
        }
        var swapIdx = 0
        while swapIdx < digits.count {
            if digits[swapIdx] != sortedDigits[swapIdx] {
                let targetIdx = numIdxMap[sortedDigits[swapIdx]]!
                digits.swapAt(targetIdx, swapIdx)
                break
            }
            swapIdx += 1
        }
        return Int(digits.reduce("") { $0 + String($1) }) ?? num
    }
}



import Foundation
// Time: O(n)
// SOurce: https://tinyurl.com/y8vqklj3
class Solution {
    func maximumSwap(_ num: Int) -> Int {
        var digits: [Int] = String(num).compactMap{ $0.wholeNumberValue }
        var numIdxMap = [Int:Int]()
        for (idx, item) in digits.enumerated() {
            numIdxMap[item] = idx
        }
        
        for currentIdx in 0..<digits.count {
            for numToSwapWith in stride(from: 9, to: digits[currentIdx], by: -1) {
                if let targetIdx = numIdxMap[numToSwapWith], targetIdx > currentIdx {
                    digits.swapAt(currentIdx, targetIdx)
                    return Int(digits.reduce("") { $0 + String($1) }) ?? num
                }
            }
        }
        return num
    }
}
