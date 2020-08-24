class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var numIdxMap = [Int:Int]()
        for i in 0..<nums.count {
            numIdxMap[nums[i]] = i
        }
        for i in 0..<nums.count {
            let num = nums[i]
            if let j = numIdxMap[target - num], j != i {
                return [i, j]
            }
        }
        return [-1, -1]
    }
}
