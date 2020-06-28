/*
// Initial solution. Time complexity: O(n^2)
class Solution {
    func checkSubarraySum(_ nums: [Int], _ k: Int) -> Bool {
        guard nums.count > 1 else {return false}
        
        for i in (0..<(nums.count) - 1) {
            var currentSum = nums[i]
            for j in ((i + 1)..<nums.count) {
                currentSum += nums[j]
                if k == 0 {
                    if currentSum == 0 {
                        print("1")
                        return true
                    } else {
                        continue
                    }
                } else if currentSum % abs(k) == 0 {
                    print("3")
                    return true
                }
            }
        }
        return false
    }
}
 */
// https://tinyurl.com/yb3ya47s
class Solution {
    func checkSubarraySum(_ nums: [Int], _ k: Int) -> Bool {
        guard nums.count > 1 else {return false}
        
        var prefixSum = 0
        var remainderMap = [-1:0] // <index:remainder>, here remainder = prefixSum % k
        for (endIdx, item) in nums.enumerated() {
            prefixSum += item
            if k != 0 {
                prefixSum = prefixSum % abs(k)
            } else {
                if (prefixSum == 0) && (endIdx) >= 1 {
                    return true
                }
            }
            
            if let startIdx = remainderMap[prefixSum] {
                if (endIdx - startIdx) > 1 {
                    return true
                }
                if (k == 0) && (prefixSum == 0) && (endIdx - startIdx) > 1 {
                    return true
                }
            }
            remainderMap[prefixSum] = endIdx
        }
        return false
    }
}
