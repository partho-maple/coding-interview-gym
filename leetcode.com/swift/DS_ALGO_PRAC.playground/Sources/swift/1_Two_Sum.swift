public class Solution {
    public func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var firstIndex = 0
        var secondIndex = 0
        var resultArr = [0, 0]
        
        for (index, value) in nums.enumerated() {
            let firstValue = value
            
            for index2 in (index + 1)..<(nums.count) {
                let secondValue = nums[index2]
                
                let sum = firstValue + secondValue
                if sum == target {
                    firstIndex = index
                    secondIndex = index2
                    resultArr = [firstIndex, secondIndex]
                    return resultArr
                }
            }
        }
        return resultArr
    }
}




/*
// Solution test code for: #1 - Two Sum
let inputArr = [0,4,3,0]
let target = 0
var solution_1 : Solution_1 = Solution_1()
solution_1.twoSum(inputArr, target)
*/
