// Brute force approach, doing an exustive search through whole state space tree, recursively
// Time limit exceeded
import Foundation
class Solution {
    func maxSumOfThreeSubarrays(_ nums: [Int], _ k: Int) -> [Int] {
        var sumIdxDict = [Int:[Int]]()
        var currentPath = [Int]()
        maxSumOfThreeSubarraysHelper(nums, k, 0, 0, 0, currentPath, &sumIdxDict)
        return sumIdxDict[sumIdxDict.keys.max()!]!
    }
    
    func maxSumOfThreeSubarraysHelper(_ nums: [Int], _ k: Int, _ startingIdx: Int, _ currentArrayCount: Int, _ currentSum: Int, _ currentPath: [Int], _ sumIdxDict: inout [Int:[Int]]) {
        if currentArrayCount >= 3 {
            guard let previousPath = sumIdxDict[currentSum] else {
                sumIdxDict[currentSum] = currentPath.sorted()
                return
            }
            if currentPath.lexicographicallyPrecedes(previousPath) {
                sumIdxDict[currentSum] = currentPath.sorted()
            }
            return
        }
        if startingIdx > (nums.count - k + 1) {
            return
        }
        for i in startingIdx..<(nums.count - k + 1) {
            let subarray = Array(nums[i..<(i+k)])
            maxSumOfThreeSubarraysHelper(nums, k, (i+k), currentArrayCount + 1, (currentSum + subarray.reduce(0, +)), currentPath + [i], &sumIdxDict)
        }
    }
}


//-----------------------------------------------------------------------------------------------------------------------------------------


import Foundation
class Solution {
    func maxSumOfThreeSubarrays(_ nums: [Int], _ k: Int) -> [Int] {
        
    }
}

//-----------------------------------------------------------------------------------------------------------------------------------------

/*
 Input: [1,2,1,2,6,7,5,1], 2
 Output: [0, 3, 5]
 Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
 We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
 
 
 map = <totalSum:[starting indices of 3 arr]>
 backtracking with resursion, can be optimised with a memo. possible DP at last to try
 1, 2, 1,2,6,7,5 ,1
 
 sumIdxDict: [
 5: [0, 1, 3],
 18: [0, 4, 6],
 10: [0, 2, 5],
 
 15: [0, 3, 5],
 
 9: [0, 2, 4],
 8: [0, 2, 6],
 4: [0, 0, 2],
 13: [0, 3, 6]]

 */

