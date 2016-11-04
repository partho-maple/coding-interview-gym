//: Playground - noun: a place where people can play

//: Problem Link:   https://leetcode.com/problems/two-sum/

import UIKit



class Solution_1 {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
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


//let inputArr = [0,4,3,0]
//let target = 0
//var solution1 = Solution1()
//    solution1.twoSum(inputArr, target)


