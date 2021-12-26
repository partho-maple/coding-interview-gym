import Foundation

// Video: https://tinyurl.com/y5bhfoze
class Solution {
    var prefixSum = [Int]()
    init(_ w: [Int]) {
        for i in 0..<w.count {
            if i == 0 {
                prefixSum.append(w[i])
            } else {
                prefixSum.append(prefixSum.last! + w[i])
            }
        }
    }
    
    func pickIndex() -> Int {
        let randWeight = Int.random(in: 1...prefixSum.last!)
        var left = 0, right = prefixSum.count - 1
        while left < right {
            let mid = left + (right - left) / 2
            if prefixSum[mid] < randWeight {
                left = mid + 1
            } else {
                right = mid
            }
        }
        
        return left
    }
}
