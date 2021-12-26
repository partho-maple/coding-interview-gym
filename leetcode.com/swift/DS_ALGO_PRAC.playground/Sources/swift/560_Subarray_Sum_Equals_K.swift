import Foundation

// Time: O(n^2)
class Solution {
    func subarraySum(_ nums: [Int], _ k: Int) -> Int {
        var prefixSum = [Int]()
        prefixSum.append(0)
        for num in nums {
            prefixSum.append(prefixSum.last! + num)
        }
        
        var count = 0
        for i in 0..<nums.count {
            for j in i..<nums.count {
                if prefixSum[j + 1] - prefixSum[i] == k {
                    count += 1
                }
            }
        }
        return count
    }
}

// Time: O(n)
import Foundation
class Solution {
    func subarraySum(_ nums: [Int], _ k: Int) -> Int {
        var prefixSumCounterMap = [Int:Int](), totalCount = 0, currentSum = 0
        prefixSumCounterMap[0] = 1
        for num in nums {
            currentSum += num
            let prevPrefixSum = currentSum - k
            if let currentCount = prefixSumCounterMap[prevPrefixSum] {
                totalCount += currentCount
            }
            prefixSumCounterMap[currentSum, default: 0] += 1
        }
        return totalCount
    }
}
