import Foundation

// Brute force. Time O(n^3)
class Solution {
    func longestSubarray(_ nums: [Int], _ limit: Int) -> Int {
        guard nums.count > 0 else {
            return 0
        }
        
        var maxLen = 1
        for i in 0..<nums.count {
            for j in i..<nums.count {
                let diff = abs(nums[i...j].max()! - nums[i...j].min()!)
                if diff <= limit {
                    maxLen = [maxLen, j - i + 1].max()!
                }
            }
        }
        return maxLen
    }
}


// Optimised Brute force. Time O(n^2)
class Solution {
    func longestSubarray(_ nums: [Int], _ limit: Int) -> Int {
        guard nums.count > 0 else {
            return 0
        }
        
        var maxLen = 1
        for i in 0..<nums.count {
            var min = Int.max
            var max = Int.min
            for j in i..<nums.count {
                min = [min, nums[j]].min()!
                max = [max, nums[j]].max()!
                let diff = abs(max - min)
                if diff <= limit {
                    maxLen = [maxLen, j - i + 1].max()!
                }
            }
        }
        return maxLen
    }
}


// Sliding Window. Time O(n). Accepted
// Source: https://tinyurl.com/y3h2fj2m
class Solution {
    func longestSubarray(_ nums: [Int], _ limit: Int) -> Int {
        guard nums.count > 0 else {
            return 0
        }
        
        var (left, right, maxLen) = (0, 0, 1)
        var (minDeque, maxDeque) = ([Int](), [Int]())
        while right < nums.count {
            while let last = minDeque.last, nums[last] >= nums[right] {
                minDeque.removeLast()
            }
            while let last = maxDeque.last, nums[last] <= nums[right] {
                maxDeque.removeLast()
            }
            minDeque.append(right)
            maxDeque.append(right)
            
            while nums[maxDeque.first!] - nums[minDeque.first!] > limit {
                left += 1
                if left > minDeque.first! {
                    minDeque.removeFirst()
                }
                if left > maxDeque.first! {
                    maxDeque.removeFirst()
                }
            }
            maxLen = [maxLen, right - left + 1].max()!
            right += 1
        }
        return maxLen
    }
}


