// https://tinyurl.com/y6s5neug
class Solution {
    func nextGreaterElements(_ nums: [Int]) -> [Int] {
        var nextGreater = Array(repeating: -1, count: nums.count), stack = [Int]()
        let len = nums.count
        for i in stride(from: 2 * len - 1, through: 0, by: -1) {
            while !stack.isEmpty && stack.last! <= nums[i % len] {
                stack.removeLast()
            }
            if !stack.isEmpty && i < len {
                nextGreater[i] = stack.last!
            }
            stack.append(nums[i % len])
        }
        return nextGreater
    }
}
