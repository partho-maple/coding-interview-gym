
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



// Time: O(n)
// https://tinyurl.com/yb3ya47s
class Solution {
    func checkSubarraySum(_ nums: [Int], _ k: Int) -> Bool {
        var modMap = [Int:Int]()
        var runningSum = 0
        modMap[runningSum] = -1
        for i in 0..<nums.count {
            let num = nums[i]
            runningSum += num
            if k != 0 {
                runningSum %= k
            }
            if let prevIdx = modMap[runningSum] {
                if i - prevIdx > 1 {
                    return true
                }
            } else {
                modMap[runningSum] = i
            }
        }
        print(modMap)
        return false
    }
}
